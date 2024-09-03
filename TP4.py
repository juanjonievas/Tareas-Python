pokemons = [
    {'numero': 1, 'nombre': 'Bulbasaur', 'tipo': ['Planta', 'Veneno'], 'nivel': 5},
    {'numero': 4, 'nombre': 'Charmander', 'tipo': ['Fuego'], 'nivel': 10},
    {'numero': 7, 'nombre': 'Squirtle', 'tipo': ['Agua'], 'nivel': 15},
    {'numero': 25, 'nombre': 'Pikachu', 'tipo': ['Electrico'], 'nivel': 20},
    {'numero': 37, 'nombre': 'Vulpix', 'tipo': ['Fuego'], 'nivel': 25},
    {'numero': 143, 'nombre': 'Snorlax', 'tipo': ['Normal'], 'nivel': 30},
    {'numero': 199, 'nombre': 'Slowking', 'tipo': ['Agua', 'Psiquico'], 'nivel': 35},
    {'numero': 1009, 'nombre': 'Mew', 'tipo': ['Psiquico'], 'nivel': 100}
]

#Funciones hash

def hash_tipo(pokemon):
    return pokemon['tipo']

def hash_numero(pokemon):
    return str(pokemon['numero'])[-1]

def hash_nivel(pokemon):
    return pokemon['nivel']

#Tablas Hash

tabla_tipo = {}
tabla_num = {}
tabla_niv = {}


def agregar_pokemon(pokemon):
    #Tipo
    for tipo in pokemon['tipo']:
        if tipo not in tabla_tipo:
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)

    #Número
    clave_num = hash_numero(pokemon)
    if clave_num not in tabla_num:
        tabla_num[clave_num] = []
    tabla_num[clave_num].append(pokemon)

    #Nivel
    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_niv:
        tabla_niv[clave_nivel] = []
    tabla_niv[clave_nivel].append(pokemon)

# e - mostrar todos los Pokemons cuyos numeros terminan en 3, 7 y 9;

def mostrarpokemonesnumero():
    for numero in tabla_num:
        if numero == '3' or numero == '7' or numero == '9':
            pokemones = tabla_num[numero]
            print(f"Pokemones que terminan en {numero}:")
            for pokemon in pokemones:
                print(pokemon)
            print()

# f - mostrar todos los Pokemons cuyos niveles son multiplos de 2, 5 y 10;

def mostrar_pokenivel():
    print(f"Pokemones con niveles multiplos de 2, 5 y 10:")
    print("")
    for nivel in tabla_niv:
        if nivel % 2 == 0 and nivel % 5 == 0 and nivel % 10 == 0:
            pokemones = tabla_niv[nivel]
            for pokemon in pokemones:
                print(pokemon)
            print()

# g - mostrar todos los Pokemons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

def mostrar_poketipo(tiposinteres):
    for tipo in tiposinteres:
        if tipo in tabla_tipo:
            pokemones = tabla_tipo[tipo]
            if pokemones:
                print(f'Pokemons de tipo: {tipo}:')
                for pokemon in pokemones:
                    print(pokemon)
                print()    
            else:
                print(f"No se encontraron Pokemones del tipo {tipo}")



for pokemon in pokemons:
    agregar_pokemon(pokemon)


print("")
print("---------------------------------------------------")
mostrarpokemonesnumero()
print("")
print("---------------------------------------------------")
mostrar_pokenivel()
print("")
print("---------------------------------------------------")
lista = ['Acero', 'Fuego', 'Electrico', 'Hielo']
mostrar_poketipo(lista)