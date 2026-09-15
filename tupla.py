#Tuplas 
tupla = ("Juan", 1.80, 94, "juan")
print(tupla) # imprime toda la tupla
print(tupla[2]) # imprime el elemento en la posición indicada 

nombre, estatura,peso, nombre_duplicado = tupla 
print(f"nombre:",[nombre_duplicado])# concatenacion de string con variable
print(f"estatura: {estatura} m") # concatenacion de string con variable
print(nombre, estatura, peso) # imprime las variables por separado  


lista_temporal = list(tupla) # convierte la tupla en una lista
print(lista_temporal) # imprime la lista temporal

lista_temporal.append("Anderson") # agrega un nuevo elemento a la lista temporal
print(lista_temporal) # imprime la lista temporal actualizada
tupla_nueva = tuple(lista_temporal) # convierte la lista temporal de nuevo a tupla
print(tupla_nueva) # imprime la nueva tupla con el nuevo elemento agregado