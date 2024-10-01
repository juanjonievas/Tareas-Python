from collections import deque

class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return f"{self.nombre} del planeta {self.planeta}"

class ColaPersonajes:
    def __init__(self):
        self.cola = deque()

    def encolar(self, personaje):
        self.cola.append(personaje)

    def desencolar(self):
        return self.cola.popleft() if self.cola else None

    def tamaño(self):
        return len(self.cola)

    def mostrar(self):
        for personaje in self.cola:
            print(personaje)

# a) Mostrar personajes del planeta Alderaan, Endor y Tatooine
def mostrar_personajes_planetas(cola):
    for personaje in cola.cola:
        if personaje.planeta in ['Alderaan', 'Endor', 'Tatooine']:
            print(personaje)

# b) Indicar el planeta natal de Luke Skywalker y Han Solo
def mostrar_planeta_luke_han(cola):
    personajes_interes = ['Luke Skywalker', 'Han Solo']
    for personaje in cola.cola:
        if personaje.nombre in personajes_interes:
            print(f"{personaje.nombre} es del planeta {personaje.planeta}")

# c) Insertar un nuevo personaje antes del maestro Yoda
def insertar_antes_de(cola, nombre_referencia, nuevo_personaje):
    temp_cola = deque()
    insertado = False

    while cola.cola:
        personaje = cola.desencolar()
        if personaje.nombre == nombre_referencia and not insertado:
            temp_cola.append(nuevo_personaje)
            insertado = True
        temp_cola.append(personaje)

    cola.cola = temp_cola

# d) Eliminar el personaje ubicado después de Jar Jar Binks
def eliminar_despues_de(cola, nombre_referencia):
    temp_cola = deque()
    eliminar_siguiente = False

    while cola.cola:
        personaje = cola.desencolar()
        if eliminar_siguiente:
            eliminar_siguiente = False  
            continue
        temp_cola.append(personaje)
        if personaje.nombre == nombre_referencia:
            eliminar_siguiente = True

    cola.cola = temp_cola

cola = ColaPersonajes()

# Agregar algunos personajes
cola.encolar(Personaje('Luke Skywalker', 'Tatooine'))
cola.encolar(Personaje('Han Solo', 'Corellia'))
cola.encolar(Personaje('Yoda', 'Dagobah'))
cola.encolar(Personaje('Leia Organa', 'Alderaan'))
cola.encolar(Personaje('Jar Jar Binks', 'Naboo'))

# a) Mostrar personajes de Alderaan, Endor, y Tatooine
print("Personajes de los planetas Alderaan, Endor y Tatooine:")
mostrar_personajes_planetas(cola)

# b) Indicar el planeta de Luke Skywalker y Han Solo
print("\nPlaneta donde reside Luke Skywalker y Han Solo:")
mostrar_planeta_luke_han(cola)

# c) Insertar un nuevo personaje antes del maestro Yoda
nuevo_personaje = Personaje('Ahsoka Tano', 'Shili')
insertar_antes_de(cola, 'Yoda', nuevo_personaje)

# d) Eliminar el personaje después de Jar Jar Binks
eliminar_despues_de(cola, 'Jar Jar Binks')

print("\nCola después de todas las operaciones:")
cola.mostrar()