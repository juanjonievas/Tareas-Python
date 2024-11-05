from arbol_avl import BinaryTree

pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["planta", "veneno"]},
    {"nombre": "Ivysaur", "numero": 2, "tipos": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipos": ["fuego"]},
    {"nombre": "Charmeleon", "numero": 5, "tipos": ["fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipos": ["agua"]},
    {"nombre": "Wartortle", "numero": 8, "tipos": ["agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["electrico"]},
    {"nombre": "Jolteon", "numero": 135, "tipos": ["electrico"]},
    {"nombre": "Magnemite", "numero": 81, "tipos": ["electrico", "acero"]},
    {"nombre": "Magneton", "numero": 82, "tipos": ["electrico", "acero"]},
    {"nombre": "Lycanroc", "numero": 745, "tipos": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["roca", "dragon"]},
    {"nombre": "Electivire", "numero": 466, "tipos": ["electrico"]},
]

# a) Arboles nombre, numero y tipo
arbol_nombre = BinaryTree()  
arbol_numero = BinaryTree()  
arbol_tipo = BinaryTree()    

# Funcion para cargar un Pokemon en los arboles
def cargar_pokemon(pokemon):
    # Insertar en arbol por nombre
    arbol_nombre.insert_node(pokemon["nombre"].lower(), pokemon)

    # Insertar en arbol por numero
    arbol_numero.insert_node(pokemon["numero"], pokemon)
    
    # Insertar en arbol por tipo
    for tipo in pokemon["tipos"]:
        tipo_nodo = arbol_tipo.search(tipo)
        if tipo_nodo is None:
            arbol_tipo.insert_node(tipo, {"pokemons": [pokemon]})
        else:
            tipo_nodo.other_value["pokemons"].append(pokemon)

# Insertar cada Pokemon de la lista en los arboles
for pokemon in pokemons:
    cargar_pokemon(pokemon)

# b) Mostrar datos de un Pokemon por numero y busqueda aproximada por nombre
def mostrar_pokemon_numero_nombre(numero, prefijo_nombre):
    print("b) Buscar Pokemon por numero y nombre parcial:")
    pokemon_encontrado = arbol_numero.search(numero)
    if pokemon_encontrado:
        print(f"Informacion del Pokemon con numero {numero}: {pokemon_encontrado.other_value}")
    
    print(f"Pokemons cuyo nombre contiene '{prefijo_nombre}':")
    arbol_nombre.proximity_search(prefijo_nombre.lower())

mostrar_pokemon_numero_nombre(4, "bul")

# c) Mostrar nombres de Pokemons de un tipo especifico
def mostrar_pokemon_tipo(tipo_pokemon):
    print(f"\nc) Pokemons de tipo {tipo_pokemon}:")
    nodo_tipo = arbol_tipo.search(tipo_pokemon)
    if nodo_tipo:
        for pokemon in nodo_tipo.other_value["pokemons"]:
            print(pokemon["nombre"])

# Ejemplos de uso para c)
mostrar_pokemon_tipo("fuego")
mostrar_pokemon_tipo("agua")
mostrar_pokemon_tipo("planta")
mostrar_pokemon_tipo("electrico")

# d) Listado en orden ascendente por numero y nombre, y por niveles en el nombre
def mostrar_ordenado_y_por_niveles():
    print("\nd) Listado ordenado por numero y nombre, y por niveles en nombre")
    
    print("Pokemons ordenados por numero:")
    def recorrido_inorden(root):
        if root:
            recorrido_inorden(root.left)
            print(f"{root.value} - {root.other_value['nombre']}")
            recorrido_inorden(root.right)
    recorrido_inorden(arbol_numero.root)
    print()

    print("Pokemons ordenados por nombre:")
    arbol_nombre.inorden()
    print()

    print("Pokemons por niveles en nombre:")
    arbol_nombre.by_level()
    print()

mostrar_ordenado_y_por_niveles()

# e) Mostrar informacion de Pokemons especificos
def mostrar_pokemon_especificos(lista_nombres):
    print("\ne) Informacion de Pokemons especificos:")
    for nombre in lista_nombres:
        nodo_pokemon = arbol_nombre.search(nombre.lower())
        if nodo_pokemon:
            print(f"Informacion de {nombre}: {nodo_pokemon.other_value}")

mostrar_pokemon_especificos(["Jolteon", "Lycanroc", "Tyrantrum"])

# f) Contar Pokemons de tipos especificos (electrico y acero)
def contar_pokemon_tipos(lista_tipos):
    print("\nf) Contar Pokemons por tipo:")
    for tipo in lista_tipos:
        nodo_tipo = arbol_tipo.search(tipo)
        cantidad = len(nodo_tipo.other_value["pokemons"]) if nodo_tipo else 0
        print(f"Total de Pokemons de tipo {tipo}: {cantidad}")

contar_pokemon_tipos(["electrico", "acero"])
