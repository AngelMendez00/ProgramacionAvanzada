from paciente import Paciente
from hospital import Hospital
from medico import Medico

hospital=Hospital()

paciente_uno=Paciente(1, "Juan", 2000, 78, 1.95, "Av. Madero")
paciente_dos=Paciente(2, "Jonathan", 2010, 70, 1.80, "Av. Madero")
medico_uno=Medico(2, "Alberto", 1993, "ALSDIl2112", "Av. Periodismo")
medico_dos=Medico(8, "Roberto", 1991, "GVHKJN3242", "Av. Periodismo")

hospital.registrar_paciente(paciente=paciente_uno)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_medico(medico=medico_uno)
hospital.registrar_medico(medico=medico_dos)

hospital.mostrar_pacientes()
hospital.mostrar_pacientes_menores()
hospital.mostrar_pacientes_mayores()
hospital.mostrar_medicos()

id_paciente_eliminar=int(input("Introduzca el id del paciente a eliminar: "))
id_medico_eliminar=int(input("Introduzca el id del medico a eliminar: "))

hospital.eliminar_paciente(id_paciente_eliminar)
hospital.eliminar_medico(id_medico_eliminar)

hospital.mostrar_pacientes()
hospital.mostrar_medicos()

hospital.registrar_consulta(id_paciente=1, id_medico=2)