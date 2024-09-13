from estudiante import Estudiante
from curso import Curso

curso_uno=Curso("Matematicas", 1234, "Tomas")
curso_dos=Curso("Español", 4321, "Santiago")
curso_tres=Curso("Historia", 8769, "Omar")

estudiante_uno=Estudiante("Juan", 19, 2222)
estudiante_dos=Estudiante("Pedro", 20, 8888)
estudiante_tres=Estudiante("Pablo", 17, 7654)

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

estudiante_uno.agregar_curso(curso_uno)
estudiante_uno.agregar_curso(curso_tres)
estudiante_dos.agregar_curso(curso_dos)
estudiante_dos.agregar_curso(curso_tres)

estudiante_uno.mostrar_informacion()
estudiante_dos.mostrar_informacion()
estudiante_tres.mostrar_informacion()