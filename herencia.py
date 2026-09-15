class persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        
    def hablar (self):
     return "hola parcero,soy una persona"
    
    def __str__(self):
     return f"Persona: {self.nombre}, Edad: {self.edad}, Altura: {self.altura}"


class empleado(persona): 
    def __init__(self, nombre, edad, altura, trabajo, salario):
        super().__init__(nombre, edad, altura)# los datos los esta sacando de la clase persona
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar (self):
     return "hola parcero, soy una perosna"
 
    def actualizar_salario(self,nuevo_salario):
        self.salario = nuevo_salario

    def __str__(self):
     return f"{super().__str__()}, Trabajo: {self.trabajo}, Salario: {self.salario}"

santiago = empleado("santiago",20,1.70,"programador",2000000)
print(santiago)

santiago.actualizar_salario(2500000)
print(santiago)

santiago.hablar()
print(santiago.hablar())


class artista(persona): 
    def __init__(self,talento):
     self.talento = talento
    
     def mostrar_talento(self):
         return f"El talento del artista es: {self.talento}"


class empleador_lista(persona,artista):
   def __init__(self,nombre,edad,altura,salario,talento, empresa):
        super().__init__(nombre,edad,altura,talento)
        # persona.__init__(self, nombre, edad, altura)
        
        
        self.salario = salario
        self.empresa = empresa
      
def hablar(self):
        return f"Hola, soy {self.nombre}, {self.mostrar_talento()} y trabajo en {self.empresa}"
    
Santiago = empleador_lista("Santiago", 20, 1.70, 2500000, "programación", "TechCorp")
print(Santiago.hablar())

# class P:
#     def hablar(self):
#         print("hola donde P")
        
