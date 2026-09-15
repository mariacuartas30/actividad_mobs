
jugadores = [
    ("Santiago Zapata", 1.81, 94),
    ("Ana López", 1.70, 65),
    ("Santiago Zapata", 1.82, 93),
    ("Carlos Ruiz", 1.90, 88),
    ("Ana López", 1.71, 64)
]

# 1. Nombres únicos (CONJUNTO)
nombres_unicos = set()

for jugador in jugadores:
    nombres_unicos.add(jugador[0])

print("Nombres únicos:", nombres_unicos)


# 2. Desempaquetado (TUPLAS)
print("\nJugadores:")
for nombre, altura, peso in jugadores:
    print("Nombre:", nombre, "| Altura:", altura, "| Peso:", peso)


# 3. Añadir posición "Pívot" (LISTA + TUPLA)
jugadores_con_posicion = []

for jugador in jugadores:
    lista_temp = list(jugador)
    lista_temp.append("Pívot")
    nueva_tupla = tuple(lista_temp)
    jugadores_con_posicion.append(nueva_tupla)

print("\nJugadores con posición:")
print(jugadores_con_posicion)


# 4. Diccionario con primera aparición (DICCIONARIO + setdefault)
dic_jugadores = {}

for jugador in jugadores_con_posicion:
    nombre, altura, peso, posicion = jugador
    dic_jugadores.setdefault(nombre, (altura, peso, posicion))

print("\nDiccionario jugadores:")
print(dic_jugadores)


# 5. Equipo por defecto (DICCIONARIO)
equipo = {}

for nombre in dic_jugadores:
    equipo.setdefault(nombre, "Tiburones")

print("\nEquipo:")
print(equipo)


# 6. Validación con frozenset (CONJUNTO)
posiciones_validas = frozenset(["Base", "Escolta", "Alero", "Ala-pívot", "Pívot"])

print("\nValidación:")
for datos in dic_jugadores.values():
    posicion = datos[2]
    print(posicion in posiciones_validas)


# 7. Actualizar jugador (update)
dic_jugadores.update({
    "Santiago Zapata": (1.85, 90, "Pívot")
})

print("\nActualizado:")
print(dic_jugadores)


# 8. Eliminar último (popitem)
eliminado = dic_jugadores.popitem()
print("\nEliminado:", eliminado)
print("Diccionario:", dic_jugadores)


# 9. Eliminar específico (del)
del dic_jugadores["Ana López"]

print("\nSin Ana López:")
print(dic_jugadores)
        
    
equipo_A = {"Santiago Zapata", "Carlos Ruiz", "María Gómez", "Luis Torres"}
equipo_B = {"Ana López", "Carlos Ruiz", "Luis Torres", "Elena Ríos"}


#Unión (A | B)
union_equipos = equipo_A | equipo_B
print("--- Unión de equipos ---")
print(union_equipos)

#Intersección (A & B)
interseccion_equipos = equipo_A & equipo_B
print("--- Intersección de equipos ---")
print(interseccion_equipos)

#Jugadores que están solo en A (A - B)
diferencia_A_B = equipo_A - equipo_B
print("--- Jugadores solo en A ---")
print(diferencia_A_B)

#Jugadores que están solo en B (B - A)
diferencia_B_A = equipo_B - equipo_A
print("--- Jugadores solo en B ---")
print(diferencia_B_A)

#Diferencia simétrica (A ^ B)
diferencia_simetrica = equipo_A ^ equipo_B
print("--- Diferencia simétrica entre equipos ---")
print(diferencia_simetrica)
