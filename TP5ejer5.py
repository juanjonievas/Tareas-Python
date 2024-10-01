class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        nuevo_nodo = Nodo(nombre, es_heroe)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar(self.raiz, nuevo_nodo)

    def _insertar(self, actual, nuevo_nodo):
        if nuevo_nodo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar(actual.derecha, nuevo_nodo)

    def listar_villanos(self):
        villanos = []
        self._listar_villanos(self.raiz, villanos)
        return sorted(villanos)

    def _listar_villanos(self, nodo, villanos):
        if nodo:
            self._listar_villanos(nodo.izquierda, villanos)
            if not nodo.es_heroe:
                villanos.append(nodo.nombre)
            self._listar_villanos(nodo.derecha, villanos)

    def listar_superheroes_con_C(self):
        heroes_con_C = []
        self._listar_superheroes_con_C(self.raiz, heroes_con_C)
        return heroes_con_C

    def _listar_superheroes_con_C(self, nodo, heroes_con_C):
        if nodo:
            self._listar_superheroes_con_C(nodo.izquierda, heroes_con_C)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                heroes_con_C.append(nodo.nombre)
            self._listar_superheroes_con_C(nodo.derecha, heroes_con_C)

    def contar_superheroes(self):
        return self._contar_superheroes(self.raiz)

    def _contar_superheroes(self, nodo):
        if nodo is None:
            return 0
        conteo = 1 if nodo.es_heroe else 0
        conteo += self._contar_superheroes(nodo.izquierda)
        conteo += self._contar_superheroes(nodo.derecha)
        return conteo

    def buscar_proximidad(self, nombre_proximo, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        if nodo.nombre.startswith(nombre_proximo):
            return nodo
        if nombre_proximo < nodo.nombre and nodo.izquierda:
            return self.buscar_proximidad(nombre_proximo, nodo.izquierda)
        elif nombre_proximo > nodo.nombre and nodo.derecha:
            return self.buscar_proximidad(nombre_proximo, nodo.derecha)
        return None

    def modificar_nombre(self, nombre_actual, nuevo_nombre):
        nodo = self.buscar_proximidad(nombre_actual)
        if nodo:
            nodo.nombre = nuevo_nombre

    def listar_superheroes_desc(self):
        heroes = []
        self._listar_superheroes(self.raiz, heroes)
        return sorted(heroes, reverse=True)

    def _listar_superheroes(self, nodo, heroes):
        if nodo:
            self._listar_superheroes(nodo.izquierda, heroes)
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self._listar_superheroes(nodo.derecha, heroes)

    def generar_bosque(self):
        arbol_superheroes = Arbol()
        arbol_villanos = Arbol()
        self._generar_bosque(self.raiz, arbol_superheroes, arbol_villanos)
        return arbol_superheroes, arbol_villanos

    def _generar_bosque(self, nodo, arbol_superheroes, arbol_villanos):
        if nodo:
            if nodo.es_heroe:
                arbol_superheroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self._generar_bosque(nodo.izquierda, arbol_superheroes, arbol_villanos)
            self._generar_bosque(nodo.derecha, arbol_superheroes, arbol_villanos)

    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)

    def barrido_alfabetico(self):
        nodos = []
        self._barrido_alfabetico(self.raiz, nodos)
        return nodos

    def _barrido_alfabetico(self, nodo, nodos):
        if nodo:
            self._barrido_alfabetico(nodo.izquierda, nodos)
            nodos.append(nodo.nombre)
            self._barrido_alfabetico(nodo.derecha, nodos)

arbol = Arbol()
arbol.insertar("Iron Man", True)
arbol.insertar("Captain America", True)
arbol.insertar("Thanos", False)
arbol.insertar("Doctor Strange", True)
arbol.insertar("Loki", False)
arbol.insertar("Black Widow", True)

# b. Listar villanos ordenados alfabéticamente
print(arbol.listar_villanos()) 
print()

# c. Mostrar todos los superhéroes que empiezan con C
print(arbol.listar_superheroes_con_C())  
print()

# d. Determinar cuántos superhéroes hay en el árbol
print(arbol.contar_superheroes()) 
print()

# e. Buscar y modificar Doctor Strange
arbol.modificar_nombre("Doctor", "Doctor Stephen Strange")
print()

# f. Listar los superhéroes ordenados de manera descendente
print(arbol.listar_superheroes_desc())  
print()

# g. Generar bosque y resolver subpuntos:
arbol_superheroes, arbol_villanos = arbol.generar_bosque()
print()

# I. Determinar cuántos nodos tiene cada árbol
print("Superhéroes:", arbol_superheroes.contar_nodos())  
print()
print("Villanos:", arbol_villanos.contar_nodos())  

# II. Barrido ordenado alfabéticamente de cada árbol
print()
print("Superhéroes :", arbol_superheroes.barrido_alfabetico())
print()
print("Villanos:", arbol_villanos.barrido_alfabetico())