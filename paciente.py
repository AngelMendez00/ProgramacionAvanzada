import random

class Paciente:
    nombre = ""
    año_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""
    id=""

    def __init__(self, id_paciente, nombre, año_nacimiento, peso, estatura, direccion):
        #self.id= random.randint(1, 1000)
        self.id=id_paciente
        self.nombre=nombre
        self.año_nacimiento=año_nacimiento
        self.peso=peso
        self.estatura=estatura
        self.direccion=direccion

    def mostrar_informacion(self):
        print("Id: ", self.id)
        print(f"Nombre: {self.nombre}")
        print(f"Año de nacimiento: {self.año_nacimiento}")
        print(f"Peso: {self.peso}")
        print(f"Estatura: {self.estatura}")
        print(f"Direccion: {self.direccion}\n")

    # @property
    # def id(self):
    #     return self.id
    # @property
    # def nombre(self):
    #     return self.nombre
    # @property
    # def año_nacimiento(self):
    #     return self.año_nacimiento
    # @property
    # def peso(self):
    #     return self.peso    
    # @property
    # def estatura(self):
    #     return self.estatura
    # @property
    # def direccion(self):
    #     return self.direccion