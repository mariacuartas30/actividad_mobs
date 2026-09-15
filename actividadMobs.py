from abc import ABC, abstractmethod


class mob(ABC):

    @abstractmethod
    def __init__(self, nombre, etapaDeLaVida):
        self.nombre = nombre
        self.etapaDeLaVida = etapaDeLaVida

    @abstractmethod
    def sonido(self):
        return "soy un mob peligroso"


class zombie(mob):

    def __init__(self, nombre, etapaDeLaVida):
        super().__init__(nombre, etapaDeLaVida)
        self._daño = 2

    def sonido(self):
        return "soy un zombie muy miedoso"

    def formaDeAtaque(self):
        return "ataco cuerpo a cuerpo"

    def drop(self):
        return "dropeo carne podrida"

    @property
    def daño(self):
        return self._daño

    @daño.setter
    def daño(self, nuevo_daño):
        self._daño = nuevo_daño


class esqueleto(mob):

    def __init__(self, nombre, etapaDeLaVida):
        super().__init__(nombre, etapaDeLaVida)

    def sonido(self):
        return "soy un esqueleto muy campero"

    def formaDeAtaque(self):
        return "ataco a larga distancia con mi arquito"

    def drop(self):
        return "dropeo hueso"

    @property
    def daño(self):
        return 4


class creeper(mob):

    def __init__(self, nombre, etapaDeLaVida):
        super().__init__(nombre, etapaDeLaVida)

    def sonido(self):
        return "kboom"

    def formaDeAtaque(self):
        return "exploto"

    def drop(self):
        return "dropeo polvora"

    @property
    def daño(self):
        return 36



creeper1 = creeper("pepeElSuicida", "adulto")
zombie1 = zombie("Legarda", "bebe")
esqueleto1 = esqueleto("piter", "adulto")


espada = input("¿El zombie tiene espada? (si/no): ")

if espada.lower() == "si":
    zombie1.daño = 5
else:
    zombie1.daño = 2


class jugador(mob):

    def __init__(self, nombre, etapaDeLaVida, vida, diamantes):
        super().__init__(nombre, etapaDeLaVida)
        self.vida = vida
        self.diamantes = diamantes

    def sonido(self):
        return "soy jugador super pro"


steve = jugador("steve", "adulto", 10, 5)


def hacer_daño(mob):
    return mob.daño


opcion = int(input(
    "steve tiene 10 corazones, selecciona que te hizo daño, "
    "1 zombie, 2 esqueleto, 3 creeper: "
))


if opcion == 1:

    daño = hacer_daño(zombie1)

    print(
        f"Te hizo daño un zombie y tu vida mermo {daño} "
        f"corazones, tu nueva vida es {steve.vida - daño}"
    )


elif opcion == 2:

    daño = hacer_daño(esqueleto1)

    print(
        f"Te hizo daño un esqueleto y tu vida mermo {daño} "
        f"corazones, tu nueva vida es {steve.vida - daño}"
    )


elif opcion == 3:

    daño = hacer_daño(creeper1)

    print(
        f"Te hizo daño un creeper y tu vida mermo {daño} "
        f"corazones, tu nueva vida es {steve.vida - daño}"
    )


else:
    print("No ingresaste ninguna de las opciones")