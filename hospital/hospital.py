from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []

    def registrar_consulta(self, id_paciente, id_medico):
        # if not self.validar_cantidad_de_usuarios():
        if self.validar_cantidad_de_usuarios() == False:
            return
        print("Validacion exitosa")

        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el medico o el paciente")
            return
        print("Continuar con el registro\n")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_medicos(self):
        print("\n-------------Medicos en el sistema---------\n")
        for medico in self.medicos:
            medico.mostrar_informacion()

    def mostrar_pacientes(self):
        print("\n-------------Pacientes en el sistema---------\n")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()

    def mostrar_pacientes_menores(self):
        print("\n-------------Pacientes menores en el sistema---------\n")
        for paciente in self.pacientes:
            if (2024-paciente.año_nacimiento) < 18:
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores(self):
        print("\n-------------Pacientes mayores en el sistema---------\n")
        for paciente in self.pacientes:
            if (2024-paciente.año_nacimiento) >= 18:
                paciente.mostrar_informacion()

    def eliminar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                self.pacientes.remove(paciente)
                print("\nPaciente con el Id ", id_paciente, " eliminado\n")
                return
        print("\nNo se encontro paciente con id ", id_paciente, "\n")

    def eliminar_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                self.medicos.remove(medico)
                print("\nMedico con el Id ", id_medico, " eliminado\n")
                return
        print("\nNo se encontro medico con id ", id_medico, "\n")

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
            
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False

    def validar_cantidad_de_usuarios(self):
        if len(self.pacientes)==0:
            print("No puedes registrar una consulta, no existen pacientes")
            return False
        
        if len(self.medicos)==0:
            print("No puedes registrar una consulta, no existen medicos")
            return False 
        return True
        
