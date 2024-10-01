class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    año_nacimiento: int

    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str, año: int):
        self.numero_control=numero_control
        self.nombre=nombre
        self.apellido=apellido
        self.rfc=rfc
        self.sueldo=sueldo
        self.año_nacimiento=año

    def mostrar_info_maestro(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        info=f"-Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}"
        return info