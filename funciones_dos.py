def verificar_clave():
    clave = input("Ingrese su clave de acceso: ")
    return clave == "1234"


def mostrar_menu():
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")


def consultar_saldo(saldo):
    print(f"Saldo actual: ${saldo:,.2f}")


def retirar_dinero(saldo):
    try:
        monto = float(input("Ingrese el monto a retirar: "))
    except ValueError:
        print("Valor no válido. Intente de nuevo.")
        return saldo

    if monto <= 0:
        print("El monto debe ser mayor a cero.")
    elif monto > saldo:
        print("Saldo insuficiente para realizar el retiro.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo:,.2f}")

    return saldo


def depositar_dinero(saldo):
    try:
        monto = float(input("Ingrese el monto a depositar: "))
    except ValueError:
        print("Valor no válido. Intente de nuevo.")
        return saldo

    if monto <= 0:
        print("El monto debe ser mayor a cero.")
    else:
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:,.2f}")

    return saldo


def ejecutar_cajero():
    if not verificar_clave():
        print("Clave incorrecta. Acceso denegado.")
        return

    saldo = 1000000.0
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = retirar_dinero(saldo)
        elif opcion == "3":
            saldo = depositar_dinero(saldo)
        elif opcion == "4":
            print("Gracias por usar el cajero automático. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_cajero()
    