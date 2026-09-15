# variables

celular1_marca = "samsumg"
celular2_marca = "apple"
celular3_marca = "huawei"

celular1_modelo = "a20"
celular2_modelo = "17 pro"
celular3_modelo = "p20 pro"

celular1_camara = "420p"
celular2_camara = "120p"
celular3_camara = "230p"

class celular ():
    marca = "samsumg"
    modelo= "a20"
    camara = "420p"
    

celular1 = celular()
print (celular1.camara)
    
#segunda clase : atributos dinamicos 
class celular2:
   def __init__(self, marca, modelo, camara):
       self.marca = marca
       self.modelo = modelo
       self.camara = camara


celular_johan = celular2("samsumg", "a20", "420p")
print(celular_johan.marca)

