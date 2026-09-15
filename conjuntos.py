conjunto = {"Juan", 1.81, 94, "Juan"}
print(conjunto) # imprime el conjunto completo

conjunto.add("Anderson") # agrega un nuevo elemento al conjunto
print(conjunto) # imprime el conjunto actualizado

conjunto.discard (94)
print(conjunto) # imprime el conjunto actualizado sin el elemento eliminado


#ejemplo con for
for caracteristica in conjunto:
    print(caracteristica) # imprime cada elemento del conjunto por separado
  
conjunto_2 = frozenset([1, 2 , 3,]) # crea un conjunto inmutable  
print(conjunto_2) # imprime el conjunto inmutable
