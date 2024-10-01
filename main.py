# -Estudaintes
# -Maestros
# -Materias
# -Horarios
# -Grupos

from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestres.semestre import Semestre
from grupos.grupo import Grupo

escuela=Escuela()

while True:
    print("\n++ Mindbox ++\n")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros")
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro")
    print("12. Eliminar materia")
    print("13. Registrar carrera")
    print("14. Registrar semestre")
    print("15. Mostrar carreras")
    print("16. Mostrar semestres")
    print("17. Mostrar grupo")
    print("18. Salir")

    opcion=input("Ingresa una opcion para continuar: ")

    if opcion == "1":
        print("\nSeleccionaste registrar estudiante\n")
        nombre= input("ingresa nombre: ")
        apellido= input("Ingresa apellido: ")
        curp= input("Ingresa curp: ")
        año= int(input("Ingresa el año de nacimiento: "))
        mes= int(input("Ingresa el mes de nacimiento: "))
        dia= int(input("Ingresa el dia de nacimiento: "))
        fecha_naciemiento= datetime(año, mes, dia)
        numero_control=escuela.generar_numero_control()

        estudiante=Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_naciemiento)
        escuela.registrar_estudiante(estudiante=estudiante)
        print("\nEstudiante registrado correctamente\n")

    elif opcion == "2":
        print("\nSeleccionaste la opcion para registrar maestro\n")
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        rfc=input("Ingrese el RFC: ")
        sueldo=float(input("Ingrese el sueldo correspondiente: "))
        año= int(input("Ingrese el año de nacimiento: "))
        numero_control=escuela.generar_numero_control_maestro(nombre=nombre, rfc=rfc, año_nacimiento=año)

        maestro=Maestro(nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo, numero_control=numero_control, año=año)
        escuela.registrar_maestro(maestro=maestro)
        print(numero_control)

    elif opcion == "3":
        print("\nSeleccionaste la opcion para registrar materia\n")
        nombre=input("Ingrese el nombre: ")
        descripcion=input("Ingrese la descripcion: ")
        semestre=int(input("Ingrese el semestre: "))
        creditos=int(input("Ingrese los creditos: "))
        id=escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)

        materia=Materia(nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos, id=id)
        escuela.registrar_materia(materia=materia)
        print(id)
        
    elif opcion == "4":
        print("\nSeleccionaste la opcion para registrar un nuevo grupo\n")

        tipo=input("Ingresa el tipo de grupo (A/B):")
        id_semestre=input("Ingresa el id del semestre al que pertenece el grupo: ")

        grupo=Grupo(tipo=tipo, id_semestre=id_semestre)

        escuela.registrar_grupo(grupo=grupo)

    elif opcion == "5":
        pass
    
    elif opcion == "6":
        escuela.listar_estudiantes()

    elif opcion == "7":
        escuela.listar_maestros()

    elif opcion == "8":
        escuela.listar_materias()

    elif opcion == "10":
        print("\nSeleccionaste eliinar estudiante\n")

        numero_control=input("Ingrese el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        print("\nSeleccionaste eliminar maestro\n")

        numero_control_maestro=input("Ingrese el numero de control del maestro a eliminar: ")
        escuela.eliminar_maestro(numero_control_maestro=numero_control_maestro)

    elif opcion == "12":
        print("\nSeleccionaste eliminar materia\n")

        id_materia=input("Ingrese el id de la materia a eliminar: ")
        escuela.eliminar_materia(id_materia=id_materia)

    elif opcion=="13":
        print("\nSeleccionaste la opcion para registrar una carrera\n")

        nombre=input("Ingresa el nombre de la carrera: ")
        carrera=Carrera(nombre=nombre)
        escuela.registrar_carrera(carrera=carrera)
        
    elif opcion=="14":
        print("\nSeleccionaste la opcion para registrar un semestre\n")

        numero=int(input("Ingresa el numero del semestre: "))
        matricula=input("Ingresa la matricula de la carrera: ")

        semestre=Semestre(numero=numero, matricula_carrera=matricula)
        escuela.registrar_semestre(semestre=semestre)

    elif opcion == "15":
        escuela.listar_carreras()

    elif opcion == "16":
        escuela.listar_semestres()

    elif opcion == "17":
        escuela.listar_grupos()
        
    elif opcion == "18":
        print("\nHasta pronto\n")
        break