superheroes = [
    {
        "nombre": "Spider-Man",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Peter Parker, un joven que obtiene habilidades arácnidas después de ser mordido por una araña radiactiva."
    },
    {
        "nombre": "Batman",
        "año_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Bruce Wayne, un millonario que combate el crimen en Gotham City usando su intelecto y habilidades físicas, con su caracteristico traje."
    },
    {
        "nombre": "Mujer Maravilla",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Diana, princesa de las Amazonas, que lucha por la justicia, el amor y la igualdad en el mundo."
    },
    {
        "nombre": "Iron Man",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Tony Stark, un genio inventor y empresario que crea una armadura avanzada para convertirse en el superhéroe Iron Man."
    },
    {
        "nombre": "Linterna Verde",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Hal Jordan, un piloto que se convierte en miembro de la Green Lantern Corps, una fuerza policial intergaláctica."
    },
    {
        "nombre": "Wolverine",
        "año_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Logan, un mutante con habilidades regenerativas y garras de adamantium."
    },
    {
        "nombre": "Doctor Strange",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Stephen Strange, un neurocirujano que se convierte en el Hechicero Supremo para proteger la Tierra contra amenazas místicas."
    },
    {
        "nombre": "Capitana Marvel",
        "año_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Carol Danvers, una ex-piloto de la Fuerza Aérea que obtiene superpoderes y se convierte en una de las heroínas más poderosas del universo."
    },
    {
        "nombre": "Flash",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Barry Allen, un científico forense que obtiene la capacidad de moverse a supervelocidad después de un accidente en su laboratorio."
    },
    {
        "nombre": "Star-Lord",
        "año_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Peter Quill, un aventurero intergaláctico y líder de los Guardianes de la Galaxia."
    },
    {
        "nombre": "Superman",
        "año_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Clark Kent, un extraterrestre del planeta Krypton que posee poderes sobrehumanos en la Tierra."
    },
    {
        "nombre": "Aquaman",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Arthur Curry, el rey de la Atlántida que tiene la capacidad de comunicarse con la vida marina y posee una fuerza sobrehumana."
    },
    {
        "nombre": "Thor",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "El dios del trueno, originario de Asgard, que protege tanto su hogar como la Tierra con su poderoso martillo Mjolnir."
    },
    {
        "nombre": "Viuda Negra",
        "año_aparicion": 1964,
        "casa_comic": "Marvel",
        "biografia": "Natasha Romanoff, una espía y asesina altamente entrenada que se convierte en una agente de S.H.I.E.L.D. y miembro de los Vengadores."
    },
    {
        "nombre": "Flecha Verde",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Oliver Queen, un millonario que combate el crimen como un arquero experto con un arco y una variedad de flechas especiales."
    }
]

# a Eliminar el nodo que contiene la información de Linterna Verde


def eliminar_superheroe(nombre):
    global superheroes
    superheroes = [hero for hero in superheroes if hero['nombre'] != nombre]


eliminar_superheroe("Linterna Verde")

# b Mostrar el año de aparición de Wolverine


def aparicion_wolverine(nombre):
    for hero in superheroes:
        if hero['nombre'] == nombre:
            return hero['año_aparicion']


print(f"Aparición de Wolverine: {aparicion_wolverine('Wolverine')}")

# c Cambiar la casa de Dr. Strange a Marvel


def cambiar_casa_superheroe(nombre, nueva_casa):
    for hero in superheroes:
        if hero['nombre'] == nombre:
            hero['casa_comic'] = nueva_casa


cambiar_casa_superheroe("Doctor Strange", "Marvel")

# d Mostrar el nombre de superhéroes que en su biografía mencionan "traje" o "armadura"


def superheroes_con_traje_o_armadura():
    return [hero['nombre'] for hero in superheroes if 'traje' in hero['biografia'].lower() or 'armadura' in hero['biografia'].lower()]


print(
    f"Superhéroes con 'traje' o 'armadura': {superheroes_con_traje_o_armadura()}")

# e Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963


def superheroes_anteriores_a(fecha):
    return [(hero['nombre'], hero['casa_comic']) for hero in superheroes if hero['año_aparicion'] < fecha]


print(f"Superhéroes anteriores a 1963: {superheroes_anteriores_a(1963)}")

# f Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla


def casa_superheroe(nombre):
    for hero in superheroes:
        if hero['nombre'] == nombre:
            return hero['casa_comic']


print(f"Casa de Capitana Marvel: {casa_superheroe('Capitana Marvel')}")
print(f"Casa de Mujer Maravilla: {casa_superheroe('Mujer Maravilla')}")

# g Mostrar toda la información de Flash y Star-Lord


def informacion_superheroe(nombre):
    for hero in superheroes:
        if hero['nombre'] == nombre:
            return hero


flash_info = informacion_superheroe("Flash")
starlord_info = informacion_superheroe("Star-Lord")
print(f"Información de Flash: {flash_info}")
print(f"Información de Star-Lord: {starlord_info}")

# h Listar los superhéroes que comienzan con la letra B, M y S


def superheroes_por_letra(letras):
    return [hero['nombre'] for hero in superheroes if hero['nombre'][0].upper() in letras]


letras_bms = ['B', 'M', 'S']
for letra in letras_bms:
    print(
        f"Superhéroes que comienzan con '{letra}': {superheroes_por_letra(letra)}")

# i Determinar cuántos superhéroes hay de cada casa de comic


def contar_superheroes_por_casa():
    count_marvel = sum(
        1 for hero in superheroes if hero['casa_comic'] == 'Marvel')
    count_dc = sum(1 for hero in superheroes if hero['casa_comic'] == 'DC')
    return {'Marvel': count_marvel, 'DC': count_dc}


print(f"Cantidad de superhéroes por casa: {contar_superheroes_por_casa()}")