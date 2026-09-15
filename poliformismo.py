#! POLIMORFISMO
#* Significa que dos objetos diferrentes pueden responder al mismo método (misma orden) de formas diferentes.
class Zombie:
    def daño(self):
        return 2
    
class Esqueleto:
    def daño(self):
        return 4
    
class Creeper:
    def daño(self):
        return 36
    
def hacer_daño(mob):
    '''A la función no le importa que clase de 'animal'. Solo le importa que tenga el método sonido()'''
    return mob.daño()
    
zombie = Zombie()
esqueleto = Esqueleto()
creeper = Creeper()


# hacer_daño(zombie)
# hacer_daño(esqueleto)
# hacer_daño(creeper)
steve=10
opcion=int(input("steve tiene 10 corazones, selecciona que te hizo daño, 1 zombie, 2 esqueleto, 3 creeper"))
if opcion==1:
    print (f"te hizo daño un zombie y tu vida mermo {hacer_daño(zombie)} corazones, tu nueva vida es {(steve-hacer_daño(zombie))}")
elif opcion ==2:
    print (f"te hizo daño un esqueleto y tu vida mermo {hacer_daño(esqueleto)} corazones, tu nueva vida es {(steve-hacer_daño(esqueleto))}")
elif opcion ==3:
    print (f"te hizo daño un creeper y tu vida mermo {hacer_daño(creeper)} corazones, tu nueva vida es {(steve-hacer_daño(creeper))} como tuvida es menor a 0 moriste")    
else:
    print("no ingresaste ninguna de las opciones ")    