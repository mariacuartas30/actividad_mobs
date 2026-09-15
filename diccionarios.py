diccionario = {
    "nombre": "Santiago",
    "estatura": 1.80,
    "peso": 94,         
    "nombre_duplicado": "Santiago"
}
print(diccionario) # imprime el diccionario completo    
print(len(diccionario)) # imprime la cantidad de elementos en el diccionario
print(diccionario["nombre"]) # imprime el valor asociado a la clave "nombre"

diccionario["edad"] = 30 # agrega una nueva clave-valor al diccionario
print(diccionario) # imprime el diccionario actualizado

del diccionario["peso"] # elimina la clave "peso" y su valor asociado
print(diccionario) # imprime el diccionario actualizado sin la clave eliminada  

"""
.keys() # devuelve una vista de las claves del diccionario

.values() # devuelve una vista de los valores del diccionario

.items() # devuelve una vista de los pares clave-valor del diccionario

.clear() # elimina todos los elementos del diccionario, dejándolo vacío

.get() # devuelve el valor asociado a una clave, o un valor predeterminado si la clave no existe

.setdefault() # devuelve el valor asociado a una clave, o establece un valor predeterminado si

.pop() # elimina una clave y devuelve su valor asociado, o un valor predeterminado si la clave no existe

.popitem() # elimina y devuelve un par clave-valor aleatorio del diccionario

.update() # actualiza el diccionario con los pares clave-valor de otro diccionario o iterable

"""
