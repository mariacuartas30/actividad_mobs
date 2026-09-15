compras = ["Leche","Pan", "Huevos", "Manzana"]

#insertar cereal en la posicion 4
compras.append("Cereal")
print(compras) 

#insertar galletas en la posicion 2
compras.insert(2,"Galletas")
print(compras)

# crear lista de ofertas y agregar a compras
ofertas = ["yogurt", "queso"]
compras.extend(ofertas)
print(compras)

#contar cuantas veces aparece pan
print(compras.count("Pan"))

#Encuentra en qué posición está "huevos"
print(compras.index("Huevos"))

#revertir la lista
compras.reverse()
print(compras)

#eliminar el último elemento de la lista
elemento_eliminado = compras.pop()
print(compras)

#eliminar el elemento uno 
compras.pop(1)
print(compras)

#borrar el elemento "leche"
if "leche" in compras:
    compras.remove("leche")
    print(compras)

#limpiar la lista
compras.clear()
print(compras)

"""#ejercicio 2"""

números = [10, 20, 30, 20, 40, 50, 20, 60]

#contar cuantas veces aparece el número 20  
print(números.count(20))

#En qué posición aparece el primer 30?
print(números.index(30))

#Elimina el último elemento y muestra cuál era.
print(números.pop())

#Elimina el elemento en la posición 2 y muestra cuál era.
print(números.pop(2))

#Eliminar la primera aparición del número 20
números.remove(20)
print(números)

#revertir la lista
números.reverse()
print(números)

#Después de invertirla, ¿en qué posición quedó el 50?
números.reverse()
print(números.index(50))

#eliminar lista
números.clear()
print(números)



