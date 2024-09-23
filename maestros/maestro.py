class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str):
        self.numero_control=numero_control
        self.nombre=nombre
        self.apellido=apellido
        self.rfc=rfc
        self.sueldo=sueldo