from random import randint

class Materia:
    id: str
    #MT{ultimos dos digitos del nombre}{semestre}{cantidad de creditos}{numero random del 1 al 1000}
    nombre: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, nombre: str, descripcion: str, semestre: int, creditos: int, id: str):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.semestre=semestre
        self.creditos=creditos

    def mostrar_info_materia(self):
        info=f"-Id: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Semestre: {self.semestre}, Creditos: {self.creditos}"
        return info