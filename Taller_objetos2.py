
# CLASE DISPOSITIVO


class Dispositivo:
    def __init__(self, tipo, marca, modelo, año_compra):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año_compra = año_compra

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año de compra: {self.año_compra}")

    def actualizar_año(self, nuevo_año):
        self.año_compra = nuevo_año



# CLASE ESTUDIANTE


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.lista_dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.lista_dispositivos.append(dispositivo)

    def mostrar_dispositivos(self):
        print(f"\nEstudiante: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Grado: {self.grado}")
        print("Dispositivos:")
        for d in self.lista_dispositivos:
            d.mostrar_info()
            print("----------------")

    def contar_dispositivos(self):
        return len(self.lista_dispositivos)



# FUNCIONES


def crear_dispositivo():
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año de compra: "))
    return Dispositivo(tipo, marca, modelo, año)


def mostrar_todos_los_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes:
        estudiante.mostrar_dispositivos()


def buscar_por_grado(lista_estudiantes, grado):
    encontrados = []
    for estudiante in lista_estudiantes:
        if estudiante.grado == grado:
            encontrados.append(estudiante)
    return encontrados


# CREACIÓN DE OBJETOS


# Dylan
dylan = Estudiante("Dylan Hinestroza", 12, "6to")
dylan.agregar_dispositivo(Dispositivo("Celular", "Samsung", "Galaxy S21", 2021))
dylan.agregar_dispositivo(Dispositivo("Tablet", "Apple", "iPad Air", 2022))

# Salome
salome = Estudiante("Salome Jiménez", 13, "7mo")
salome.agregar_dispositivo(Dispositivo("Laptop", "HP", "Pavilion", 2023))
salome.agregar_dispositivo(Dispositivo("Celular", "Xiaomi", "Redmi Note 10", 2022))

# Alejandro
alejandro = Estudiante("Alejandro Varela", 11, "5to")
alejandro.agregar_dispositivo(Dispositivo("Tablet", "Lenovo", "Tab P11", 2023))

lista_estudiantes = [dylan, salome, alejandro]

# MOSTRAR TODOS


print("===== ESTUDIANTES Y DISPOSITIVOS =====")
mostrar_todos_los_estudiantes(lista_estudiantes)


# BUSCAR POR GRADO


grado = input("\nIngrese el grado a buscar: ")
resultado = buscar_por_grado(lista_estudiantes, grado)

print("\nEstudiantes encontrados:")
for estudiante in resultado:
    print(estudiante.nombre)


# NUEVO ESTUDIANTE


print("\n=== Registrar nuevo estudiante ===")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
grado = input("Grado: ")

nuevo = Estudiante(nombre, edad, grado)
lista_estudiantes.append(nuevo)


# AGREGAR DISPOSITIVO


nombre_buscar = input("\nNombre del estudiante para agregar dispositivo: ")

for estudiante in lista_estudiantes:
    if estudiante.nombre.lower() == nombre_buscar.lower():
        dispositivo = crear_dispositivo()
        estudiante.agregar_dispositivo(dispositivo)
        print("Dispositivo agregado.")


# ESTUDIANTES CON MÁS DE 2 DISPOSITIVOS


contador = 0

for estudiante in lista_estudiantes:
    if estudiante.contar_dispositivos() > 2:
        contador += 1

print("\nEstudiantes con más de 2 dispositivos:", contador)