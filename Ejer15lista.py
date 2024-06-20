entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "pokemones": [
            {"nombre": "Pikachu", "nivel": 80, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Bulbasaur", "nivel": 65,"tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Squirtle", "nivel": 60, "tipo": "Agua", "subtipo": None},
            {"nombre": "Greninja", "nivel": 90, "tipo": "Agua", "subtipo": "Siniestro"}
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemones": [
            {"nombre": "Cinderace", "nivel": 75, "tipo": "Fuego", "subtipo": None},
            {"nombre": "Flygon", "nivel": 70, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Golurk", "nivel": 65,"tipo": "Tierra", "subtipo": "Fantasma"},
            {"nombre": "Sobble", "nivel": 50, "tipo": "Agua", "subtipo": None},
            {"nombre": "Scyther", "nivel": 60, "tipo": "Bicho", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "pokemones": [
            {"nombre": "Charizard", "nivel": 100, "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Rillaboom", "nivel": 85,"tipo": "Planta", "subtipo": None},
            {"nombre": "Haxorus", "nivel": 88, "tipo": "Dragón", "subtipo": None}
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "pokemones": [
            {"nombre": "Eevee", "nivel": 45, "tipo": "Normal", "subtipo": None},
            {"nombre": "Espeon", "nivel": 55, "tipo": "Psíquico", "subtipo": None}
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "pokemones": [
            {"nombre": "Duraludon", "nivel": 85, "tipo": "Acero", "subtipo": "Dragón"},
            {"nombre": "Flygon", "nivel": 80, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Garchomp", "nivel": 85,"tipo": "Dragón", "subtipo": "Tierra"},
            {"nombre": "Togekiss", "nivel": 75, "tipo": "Hada", "subtipo": "Volador"},
            {"nombre": "Tyranitar", "nivel": 82, "tipo": "Roca", "subtipo": "Siniestro"}
        ]
    }
]

# a Obtener la cantidad de Pokémons de un determinado entrenador


def cantidad_pokemones(nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            return len(entrenador['pokemones'])
    return 0


print(
    f"Cantidad de Pokémons de Ash Ketchum: {cantidad_pokemones('Ash Ketchum')}")

# b Listar los entrenadores que hayan ganado más de tres torneos


def entrenadores_mas_de_tres_torneos():
    return [entrenador['nombre'] for entrenador in entrenadores if entrenador['torneos_ganados'] > 3]


print(
    f"Entrenadores que han ganado más de tres torneos: {entrenadores_mas_de_tres_torneos()}")

# c El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados


def pokemon_mas_nivel_entrenador_mas_torneos():
    entrenador_max_torneos = max(
        entrenadores, key=lambda e: e['torneos_ganados'])
    pokemon_mas_nivel = max(
        entrenador_max_torneos['pokemones'], key=lambda p: p['nivel'])
    return pokemon_mas_nivel


print(
    f"Pokemon de mayor nivel del entrenador con más torneos ganados: {pokemon_mas_nivel_entrenador_mas_torneos()}")

# d Mostrar todos los datos de un entrenador y sus Pokémon


def datos_entrenador_y_pokemones(nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            return entrenador


print(
    f"Datos de Ash Ketchum y sus Pokémons: {datos_entrenador_y_pokemones('Ash Ketchum')}")

# e Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%


def entrenadores_porcentaje_batallas_ganadas_mas_79():
    return [entrenador['nombre'] for entrenador in entrenadores if (entrenador['batallas_ganadas'] / (entrenador['batallas_ganadas'] + entrenador['batallas_perdidas'])) > 0.79]


print(
    f"Entrenadores con porcentaje de batallas ganadas mayor al 79%: {entrenadores_porcentaje_batallas_ganadas_mas_79()}")

# f Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)


def entrenadores_pokemones_tipo_especifico(tipo, subtipo):
    return [entrenador['nombre'] for entrenador in entrenadores
            if any((pokemon['tipo'] == tipo and (pokemon['subtipo'] == subtipo or subtipo is None)) for pokemon in entrenador['pokemones'])]


print(
    f"Entrenadores con Pokémons de tipo fuego y planta o agua/volador: {entrenadores_pokemones_tipo_especifico('Fuego', None)}")

# g El promedio de nivel de los Pokémons de un determinado entrenador


def promedio_nivel_pokemones_entrenador(nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            pokemones = entrenador['pokemones']
            if len(pokemones) > 0:
                return sum(pokemon['nivel'] for pokemon in pokemones) / len(pokemones)
    return 0


print( 
    f"Promedio de nivel de los Pokémons de Ash Ketchum: {promedio_nivel_pokemones_entrenador('Ash Ketchum')}")

# h Determinar cuántos entrenadores tienen a un determinado Pokémon


def contar_entrenadores_con_pokemon(nombre_pokemon):
    count = 0
    for entrenador in entrenadores:
        for pokemon in entrenador['pokemones']:
            if pokemon['nombre'] == nombre_pokemon:
                count += 1
    return count


print(
    f"Cantidad de entrenadores con el Pokémon 'Flygon': {contar_entrenadores_con_pokemon('Flygon')}")

# i Mostrar los entrenadores que tienen Pokémons repetidos


def entrenadores_con_pokemones_repetidos():
    pokemon_set = set()
    entrenadores_con_repetidos = set()

    for entrenador in entrenadores:
        for pokemon in entrenador['pokemones']:
            nombre_pokemon = pokemon['nombre']
            if nombre_pokemon in pokemon_set:
                entrenadores_con_repetidos.add(entrenador['nombre'])
            else:
                pokemon_set.add(nombre_pokemon)

    return list(entrenadores_con_repetidos)


print(
    f"Entrenadores con Pokémons repetidos: {entrenadores_con_pokemones_repetidos()}")

# j Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull


def entrenadores_con_pokemones_especificos(pokemones_especificos):
    return [entrenador['nombre'] for entrenador in entrenadores
            if any(pokemon['nombre'] in pokemones_especificos for pokemon in entrenador['pokemones'])]


pokemones_especificos = ['Tyrantrum', 'Terrakion', 'Wingull']
print(
    f"Entrenadores con los Pokémons {pokemones_especificos}: {entrenadores_con_pokemones_especificos(pokemones_especificos)}")

# k Determinar si un entrenador "X" tiene al Pokémon "Y"


def entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] == nombre_pokemon:
                    return True, entrenador, pokemon
            return False, None, None
    return False, None, None


entrenador_buscar = "Ash Ketchum"
pokemon_buscar = "Pikachu"
encontrado, datos_entrenador, datos_pokemon = entrenador_tiene_pokemon(
    entrenador_buscar, pokemon_buscar)
if encontrado:
    print(
        f"El entrenador {datos_entrenador['nombre']} tiene al Pokémon {datos_pokemon['nombre']}. Detalles: {datos_entrenador}, {datos_pokemon}")
else:
    print(
        f"El entrenador {entrenador_buscar} no tiene al Pokémon {pokemon_buscar}.")