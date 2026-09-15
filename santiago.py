import random

# --- DATOS INICIALES ---
datos_brutos = [
    ("Sergio Fajardo", 1.81, 94),
    ("Paloma velasquez", 1.70, 65),
    ("Sergio Fajardo", 1.82, 93),
    ("Carlos Vives", 1.90, 88),
    ("Paloma velasquez", 1.71, 64),
    ("María Gómez", 1.75, 70),
    ("Luis Torres", 1.88, 85)
]

POSICIONES = ("defensa", "portero", "lateral", "volante", "delantero")


# ---------------------------------------------------
# FUNCION PARA LIMPIAR NOMBRES REPETIDOS
# ---------------------------------------------------
def obtener_nombres_unicos(datos):
    
    nombres_unicos = set()

    for jugador in datos:
        nombres_unicos.add(jugador[0])

    return nombres_unicos


# ---------------------------------------------------
# FUNCION PARA CREAR EL REGISTRO DE JUGADORES
# ---------------------------------------------------
def crear_registro_jugadores(datos, nombres):

    registro_jugadores = {}

    for nombre in nombres:

        for j_nom, j_alt, j_pes in datos:

            if j_nom == nombre:

                registro_jugadores[nombre] = {
                    "altura": j_alt,
                    "peso": j_pes,
                    "posicion": POSICIONES[4]
                }

                break

    return registro_jugadores


# ---------------------------------------------------
# FUNCION PARA MOSTRAR EL MENU
# ---------------------------------------------------
def mostrar_menu():

    print("\n--- MENU PRINCIPAL ---")
    print("1. Agregar jugador a un equipo")
    print("2. Consultar información de un jugador")
    print("3. Jugar partido")
    print("4. Ver tabla de posiciones")
    print("5. Salir")


# ---------------------------------------------------
# FUNCION PARA AGREGAR JUGADOR
# ---------------------------------------------------
def agregar_jugador(registro_jugadores, equipos):

    nombre_j = input("Nombre del jugador: ")
    nombre_e = input("Nombre del equipo: ")

    if nombre_j not in registro_jugadores:

        print("Error: El jugador no existe en el registro.")

    elif nombre_e not in equipos:

        print("Error: El equipo no existe.")

    else:

        ya_tiene_equipo = False

        for lista_jugadores in equipos.values():

            if nombre_j in lista_jugadores:

                ya_tiene_equipo = True
                break

        if ya_tiene_equipo:

            print(f"Error: {nombre_j} ya pertenece a un equipo.")

        else:

            equipos[nombre_e].append(nombre_j)

            print(f"¡{nombre_j} ha sido agregado a {nombre_e}!")


# ---------------------------------------------------
# FUNCION PARA CONSULTAR JUGADOR
# ---------------------------------------------------
def consultar_jugador(registro_jugadores, equipos):

    nombre_j = input("Ingrese el nombre exacto del jugador: ")

    if nombre_j in registro_jugadores:

        datos = registro_jugadores[nombre_j]

        print(f"Altura: {datos['altura']}m")
        print(f"Peso: {datos['peso']}kg")
        print(f"Posición: {datos['posicion']}")

        pertenece = "Ninguno"

        for eq, integrantes in equipos.items():

            if nombre_j in integrantes:

                pertenece = eq
                break

        print(f"Equipo: {pertenece}")

    else:

        print("Jugador no encontrado.")


# ---------------------------------------------------
# FUNCION PARA JUGAR PARTIDO
# ---------------------------------------------------
def jugar_partido(equipos, registro_jugadores, victorias, historial_partidos):

    puntajes_finales = {}

    for eq, integrantes in equipos.items():

        suma_alturas_cm = 0

        for p in integrantes:

            suma_alturas_cm += registro_jugadores[p]["altura"] * 100

        puntajes_finales[eq] = suma_alturas_cm + random.randint(0, 20)

    p1 = puntajes_finales["Deportivo aguas claras"]
    p2 = puntajes_finales["Independiente barrancabermeja"]

    print(f"\nRESULTADO:")
    print(f"Aguas Claras ({p1}) vs Barrancabermeja ({p2})")

    resultado_texto = ""

    if p1 > p2:

        resultado_texto = f"Ganador: Deportivo aguas claras ({p1} - {p2})"

        victorias["Deportivo aguas claras"] += 1

    elif p2 > p1:

        resultado_texto = f"Ganador: Independiente barrancabermeja ({p2} - {p1})"

        victorias["Independiente barrancabermeja"] += 1

    else:

        resultado_texto = f"Empate ({p1} - {p2})"

    print(resultado_texto)

    historial_partidos.append(resultado_texto)


# ---------------------------------------------------
# FUNCION PARA MOSTRAR TABLA
# ---------------------------------------------------
def mostrar_tabla(victorias):

    lista_ordenada = sorted(
        victorias.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\n--- TABLA DE POSICIONES ---")

    for eq, vics in lista_ordenada:

        print(f"{eq}: {vics} victorias")


# ---------------------------------------------------
# FUNCION PARA MOSTRAR HISTORIAL
# ---------------------------------------------------
def mostrar_historial(historial_partidos):

    print("\n--- RESUMEN FINAL DE PARTIDOS ---")

    if not historial_partidos:

        print("No se jugaron partidos.")

    else:

        for partido in historial_partidos:

            print(partido)


# ---------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------

# LIMPIAR NOMBRES
nombres_unicos = obtener_nombres_unicos(datos_brutos)

# CREAR REGISTRO
registro_jugadores = crear_registro_jugadores(
    datos_brutos,
    nombres_unicos
)

# EQUIPOS
equipos = {
    "Deportivo aguas claras": [],
    "Independiente barrancabermeja": []
}

# VICTORIAS
victorias = {
    "Deportivo aguas claras": 0,
    "Independiente barrancabermeja": 0
}

# HISTORIAL
historial_partidos = []


# ---------------------------------------------------
# MENU PRINCIPAL
# ---------------------------------------------------
while True:

    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        agregar_jugador(
            registro_jugadores,
            equipos
        )

    elif opcion == "2":

        consultar_jugador(
            registro_jugadores,
            equipos
        )

    elif opcion == "3":

        jugar_partido(
            equipos,
            registro_jugadores,
            victorias,
            historial_partidos
        )

    elif opcion == "4":

        mostrar_tabla(victorias)

    elif opcion == "5":

        mostrar_historial(historial_partidos)

        print("Saliendo del programa...")
        break

    else:

        print("Opción no válida.")