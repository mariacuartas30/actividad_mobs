
class perros:
    def __init__(self, raza, color, peso, edad):
        self.raza = raza
        self.color = color
        self.peso = peso
        self.edad = edad
        

    def correr (self):
        print(f"el perro es de raza {self.raza} va a correr")
    
    def saltar(self):
      print(f"el {self.raza} va a saltar ")
      

perroDeJohanYSalome = perros("hosky", "blanco", 57, 5)
print(f"el perro pesa {perroDeJohanYSalome.peso} {perroDeJohanYSalome.correr()}")

perraDeJohanYSalome = perros("pomerania", "blanco ", 40, 3)
print(f"el perro es de raza {perraDeJohanYSalome.raza} y tiene {perraDeJohanYSalome.edad} años")

perraDeJohanYSalome2 = perros("Doberman", "negro ", 54, 2)
print(perraDeJohanYSalome2.color)


#preguntar al usuario su informacion 
racita=input("ingrese la raza: ")
coloscito=input("ingrese su color: ")
pesito=input("ingrese su peso: ")
edadsita=input("ingrese la edad: ")
  
perroDeElUsuario=perros(racita, coloscito, pesito, edadsita)
print(perroDeElUsuario.saltar())

