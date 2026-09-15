#En una tienda de juegos de mesa hay 20 cartas disponibles, numeradas del 1 al 20. Cada jugador debe recibir 5 cartas diferentes, elegidas al azar, para formar su mano. El programa debe:
#Generar un conjunto con todos los números del 1 al 20 (las cartas disponibles).
#Seleccionar aleatoriamente 5 cartas para el Jugador 1 y 5 cartas para el Jugador 2, ambas sin repetir dentro de cada mano (usando conjuntos).
#Mostrar:
#Las cartas del Jugador 1.
#Las cartas del Jugador 2.
#Las cartas que ambos jugadores tienen en común (si existen).
#La cantidad total de cartas que tienen en común.

import random

# Cartas disponibles
cartas_disponibles = set(range(1, 21))

# Cada jugador recibe 5 cartas diferentes
jugador_1 = set(random.sample(list(cartas_disponibles), 5))
jugador_2 = set(random.sample(list(cartas_disponibles), 5))

# Cartas en común
cartas_comunes = jugador_1 & jugador_2

print("Cartas del Jugador 1:", sorted(jugador_1))
print("Cartas del Jugador 2:", sorted(jugador_2))
print("Cartas en común:", sorted(cartas_comunes) if cartas_comunes else "Ninguna")
print("Cantidad total de cartas en común:", len(cartas_comunes))

