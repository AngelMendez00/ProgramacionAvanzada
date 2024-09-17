import random

class Medico:
    nombre = ""
    año_nacimiento = 0
    rfc=""
    direccion = ""
    id=0

    def __init__(self, id_medico, nombre, año_nacimiento, rfc, direccion):
        #self.id= random.randint(1, 1000)
        self.id=id_medico
        self.nombre=nombre
        self.año_nacimiento=año_nacimiento
        self.direccion=direccion
        self.rfc=rfc

    def mostrar_informacion(self):
        print("Id: ", self.id)
        print(f"Nombre: {self.nombre}") 
        print(f"Año de nacimiento: {self.año_nacimiento}")
        print(f"RFC: {self.rfc}")
        print(f"Direccion: {self.direccion}\n")

    # @property
    # def id(self):
    #     return self.id
    # @id.setter
    # def id(self, id_nuevo):
    #     self.id=id_nuevo
    # @property
    # def nombre(self):
    #     return self.nombre
    # @property
    # def año_nacimiento(self):
    #     return self.año_nacimiento
    # @property
    # def rfc(self):
    #     return self.rfc    
    # @property
    # def direccion(self):
    #     return self.direccion