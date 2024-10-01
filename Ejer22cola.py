from collections import deque

class PersonajeMCU:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_personaje} ({self.nombre_superheroe}) - {self.genero}"

class ColaPersonajesMCU:
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

# a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
def buscar_personaje_por_superheroe(cola, nombre_superheroe):
    for personaje in cola.cola:
        if personaje.nombre_superheroe == nombre_superheroe:
            return personaje.nombre_personaje
    return None

# b) Mostrar los nombres de los superhéroes femeninos
def mostrar_superheroinas(cola):
    for personaje in cola.cola:
        if personaje.genero == 'F':
            print(f"Superheroína: {personaje.nombre_superheroe}")

# c) Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    for personaje in cola.cola:
        if personaje.genero == 'M':
            print(f"Personaje masculino: {personaje.nombre_personaje}")

# d) Determinar el nombre del superhéroe del personaje Scott Lang
def buscar_superheroe_por_personaje(cola, nombre_personaje):
    for personaje in cola.cola:
        if personaje.nombre_personaje == nombre_personaje:
            return personaje.nombre_superheroe
    return None

# e) Mostrar los datos de los personajes o superhéroes cuyos nombres comienzan con la letra S
def mostrar_nombres_con_s(cola):
    for personaje in cola.cola:
        if personaje.nombre_personaje.startswith('S') or personaje.nombre_superheroe.startswith('S'):
            print(personaje)

# f) Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su superhéroe
def buscar_carol_danvers(cola):
    for personaje in cola.cola:
        if personaje.nombre_personaje == 'Carol Danvers':
            return f"Carol Danvers es {personaje.nombre_superheroe}"
    return "Carol Danvers no está en la cola."


cola = ColaPersonajesMCU()

cola.encolar(PersonajeMCU('Tony Stark', 'Iron Man', 'M'))
cola.encolar(PersonajeMCU('Steve Rogers', 'Capitán América', 'M'))
cola.encolar(PersonajeMCU('Natasha Romanoff', 'Black Widow', 'F'))
cola.encolar(PersonajeMCU('Carol Danvers', 'Capitana Marvel', 'F'))
cola.encolar(PersonajeMCU('Scott Lang', 'Ant-Man', 'M'))
cola.encolar(PersonajeMCU('Wanda Maximoff', 'Scarlet Witch', 'F'))

# a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
print("a) Nombre Capitana Marvel:", buscar_personaje_por_superheroe(cola, 'Capitana Marvel'))

# b) Mostrar los nombres de los superhéroes femeninos
print("\nb) Superheroínas:")
mostrar_superheroinas(cola)

# c) Mostrar los nombres de los personajes masculinos
print("\nc) Personajes masculinos:")
mostrar_personajes_masculinos(cola)

# d) Determinar el nombre del superhéroe del personaje Scott Lang
print("\nd) Superhéroe de Scott Lang:", buscar_superheroe_por_personaje(cola, 'Scott Lang'))

# e) Mostrar los datos de los personajes o superhéroes cuyos nombres comienzan con la letra S
print("\ne) Personajes o superhéroes que empiezan con S:")
mostrar_nombres_con_s(cola)
print()

# f) Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
print(buscar_carol_danvers(cola))
