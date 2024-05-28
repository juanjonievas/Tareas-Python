
class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None
    
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None
    
    def tamano(self):
        return len(self.items)

pila_ep_v = Pila()
personajes_ep_v = ["Chewbacca", "Leia Organa", "Han Solo", "C-3PO", "Yoda"]
for personaje in personajes_ep_v:
    pila_ep_v.apilar(personaje)

pila_ep_vii = Pila()
personajes_ep_vii = ["Lor San Tekka", "Finn", "Han Solo", "Leia Organa", "Kylo Ren"]
for personaje in personajes_ep_vii:
    pila_ep_vii.apilar(personaje)

def Conjunto_de_pilas(pila1,pila2):
    Nombres1=set()
    while not pila1.esta_vacia():
        Nombres1.add(pila1.desapilar())

    Nombres2=set()
    while not pila2.esta_vacia():
        Nombres2.add(pila2.desapilar())

    interseccion = Nombres1.intersection(Nombres2)

    Nombre_en_ambos = Pila()
    for personaje in interseccion:
        Nombre_en_ambos.apilar(personaje)

    return Nombre_en_ambos

Nombre_en_ambos = Conjunto_de_pilas(pila_ep_v, pila_ep_vii)

print("Personajes que estuvieron en ambos episodios:")
while not Nombre_en_ambos.esta_vacia():
    print( Nombre_en_ambos.desapilar())