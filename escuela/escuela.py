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

    def listar_estudiantes(self):
        print("\n---ESTUDIANTES---\n")
        for estudainte in self.lista_estudiantes:
            print(estudainte.mostrar_info_estudiante())  

    def listar_maestros(self):
        print("\n---MAESTROS---\n")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())  

    def listar_materias(self):
        print("\n---MATERIAS---\n")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if numero_control==estudiante.numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("\nEstudiante eliminado\n")
                return
        print("\nEstudiante no encontrado\n")

    def eliminar_maestro(self, numero_control_maestro):
        for maestro in self.lista_maestros:
            if numero_control_maestro==maestro.numero_control:
                self.lista_maestros.remove(maestro)
                print("\nMaestro eliminado\n")
                return
        print("\nMaestro no encontrado\n")

    def eliminar_materia(self, id_materia):
        for materia in self.lista_materias:
            if id_materia==materia.id:
                self.lista_materias.remove(materia)
                print("\nMateria eliminada\n")
                return
        print("\nMateria no encontrada\n")
    #listar para maestro y materia, ademas, eliminar para maestro y materia 

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
