#Desarrollar una función que permita convertir un número romano en un número decimal.
def romano(numero):
    valor = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(numero)==0:
        return 0
    
    if len(numero) == 1:
        return valor[numero]

    if valor[numero[0]] < valor[numero[1]]:
        return valor[numero[1]] - valor[numero[0]] + romano(numero[2:])
    else:
        return valor[numero[0]] + romano(numero[1:])
    
    