def lista_Nombres_inversa(lista):
    if len(lista) == 0: #Se podria hacer con un not también
        return []
    else:
        return lista_Nombres_inversa(lista[1:]) + [lista[0]] 

mi_lista = ["Juan", "Arbol", "Pedro", "Matias", "José"]
print(lista_Nombres_inversa(mi_lista))

