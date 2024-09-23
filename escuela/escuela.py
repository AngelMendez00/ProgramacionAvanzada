from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_grupos: List[Grupo] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def generar_numero_control(self):
        mes=datetime.now().month
        año=datetime.now().year
        numero_control=f"L{año}{mes}{(len(self.lista_estudiantes)+1)}{randint(1, 10000)}"
        return numero_control
    
    def generar_numero_control_maestro(self, nombre, rfc, año_nacimiento):
        dia=datetime.now().day
        digitos_nombre=nombre[0:2].upper()
        digitos_rfc=rfc[-2:].upper()
        numero_control=f"M{año_nacimiento}{dia}{randint(500, 5000)}{digitos_nombre}{digitos_rfc}{(len(self.lista_maestros)+1)}"
        return numero_control
    
    def generar_id_materia(self, nombre, semestre, creditos):
        digitos_nombre=nombre[-2:].upper()
        id=f"MT{digitos_nombre}{semestre}{creditos}{randint(1, 1000)}"
        return id
