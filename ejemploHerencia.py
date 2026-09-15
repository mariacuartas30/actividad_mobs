
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        return "Guau guau guau"

    def __str__(self):
        return f"Perro: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}"


class PastorAleman(Perro):
    def __init__(self, nombre, edad, raza, color, tamaño):
        super().__init__(nombre, edad, raza)
        self.color = color
        self.tamaño = tamaño

    def ladrar(self):
        return "Guau guau guau guau"

    def __str__(self):
        return f"{super().__str__()}, Color: {self.color}, Tamaño: {self.tamaño}"


Rocki = PastorAleman(
    "Rocki",
    3,
    "Pastor Alemán",
    "Negro y marrón",
    "Grande"
)

print(Rocki)
print(Rocki.ladrar())


class Hoscky(Perro):
    def __init__(self, talento):
        self.talento = talento

    def mostrar_talento(self):
        return f"El talento del Hoscky es {self.talento}"


class Perro_lista(Perro, Hoscky):
    def __init__(self, nombre, edad, raza, talento):
        Perro.__init__(self, nombre, edad, raza)
        self.talento = talento

    def mostrar_talento(self):
        return f"El talento del perro es {self.talento}"

    def hablar(self):
        return f"El perro se llama {self.nombre}, {self.mostrar_talento()}"



Rocky = Perro_lista(
    "Rocky",
    3,
    "Husky",
    "Brincar"
)

print(Rocky)
print(Rocky.ladrar())
print(Rocky.hablar())
