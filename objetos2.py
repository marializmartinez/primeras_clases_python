
class Dino:
    patas = 4
    nombre = None
    def __init__(self, canti_patas, un_nombre):
        self.patas = canti_patas
        self.nombre = un_nombre
        print ("Hola soy un dinosuario", ", me llamo", self.nombre, " y tengo, ", self.patas)
    def get_patas(self):
        return self.patas
    def set_patas(self, cantidad):
        self.patas = cantidad
pepito = Dino(4, "Pepito")

    
#//////////// Ejercicio /////////////
# En el archivo persona.py Crear una clase Persona con atributo nombre
# Después instanciar un objeto de tipo persona.

class  Persona:
    nombre = None
    def  __init__(self, un_nombre):
        self.nombre = un_nombre
        print ("Dime tu nombre:", self.nombre)

usuario_nombre = Persona("nose")







