mochila=["Medicina","Botas","Comida","sable de luz","Casco","Guantes"]
def usar_la_fuerza(mochila, i=0):
    if i>=len(mochila):
            return ("El sable no esta en la mochila y se sacaron todos los objetos")
    elif mochila[i]=="sable de luz":
        return ("encontre el sable y tuve que sacar solo ", i , "objetos")
    
    else:
        return usar_la_fuerza (mochila, i+1 )
    
        
print (usar_la_fuerza(mochila))