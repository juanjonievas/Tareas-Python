
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
    
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]
    
#Contar cuantas especies hay:

def contar_especies(dinosaurios):
    especies = set()
    for dino in dinosaurios:
        especies.add(dino["especie"])
    return len(especies)


#Determinar cuantos descubridores distintos hay:
def contar_descubridores(dinosaurios):
    descubridores = set()
    for dino in dinosaurios:
        descubridores.add(dino["descubridor"])
    return len(descubridores)


#Mostrar todos los dinosaurios que empiecen con T
def mostrar_dinosaurios_con_t(dinosaurios):
    for dino in dinosaurios:
        if dino["nombre"].startswith("T"):
            print(dino["nombre"])


#Mostrar todos los dinosaurios que pesen menos de 275 Kg
def Dinosaurios_menores275_KG(dinosaurios):
    for dino in dinosaurios:
        peso_str = dino["peso"].split()[0]  
        peso = int(peso_str) if peso_str.isdigit() else None 
        if peso is not None and peso < 275:
            print(dino["nombre"])


#lista aparte todos los dinosaurios que comienzan con A, Q, S
def Dinosaurios_con_A_Q_S(dinosaurios):
    lista_aparte_de_dinosaurios = []
    for dino in dinosaurios:
        if dino["nombre"][0].upper() in ['A', 'Q', 'S']:
            lista_aparte_de_dinosaurios.append(dino)
    return lista_aparte_de_dinosaurios

#A)
print("Cantidad de especies:", contar_especies(dinosaurios))
#B)
print("Cantidad de descubridores distintos:", contar_descubridores(dinosaurios))

#C)
print("Dinosaurios que empiezan con T:")
mostrar_dinosaurios_con_t(dinosaurios)

#D)
print("Dinosaurios que pesan menos de 275 Kg:")
Dinosaurios_menores275_KG(dinosaurios)
#E)
print("Dinosaurios que comienzan con A, Q, S:")
dinosaurios_separados = Dinosaurios_con_A_Q_S(dinosaurios)
for dino in dinosaurios_separados:
    print(dino["nombre"])







