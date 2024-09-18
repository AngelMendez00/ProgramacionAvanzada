import random

class Paciente:
    nombre: str
    año_nacimiento: int
    peso: float
    estatura: float
    direccion: str
    id: int

    def __init__(self, nombre: str, año_nacimiento: int, peso: float, estatura: float, direccion: str):
        self.id= random.randint(1, 1000)
        self.nombre=nombre
        self.año_nacimiento=año_nacimiento
        self.peso=peso
        self.estatura=estatura
        self.direccion=direccion

    def mostrar_informacion(self) -> None:
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