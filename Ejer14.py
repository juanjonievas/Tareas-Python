series = [ {"nombre": "Los 100", "temporadas": 7, "capitulos": 100},
           {"nombre": "Star Wars:Rebels", "temporadas": 4, "capitulos": 75},
           {"nombre": "game of thrones", "temporadas": 8, "capitulos": 73},
           {"nombre": "Ley de los audaces", "temporadas": 9, "capitulos": 134},
           {"nombre": "Dr. House", "temporadas": 8, "capitulos": 177} ]

def listar_series_por_criterio(series, criterio):
    return sorted(series, key=lambda x: x[criterio])

# Ejemplo de uso:
series_por_nombre = listar_series_por_criterio(series, "nombre")
series_por_temporadas = listar_series_por_criterio(series, "temporadas")
series_por_capitulos = listar_series_por_criterio(series, "capitulos")