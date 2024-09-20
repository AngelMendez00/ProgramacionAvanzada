# -Estudaintes
# -Maestros
# -Materias
# -Horarios
# -Grupos

from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro

escuela=Escuela()

while True:
    print("++ Mindbox ++")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar grupo")
    print("4. Registrar materia")
    print("5. Registrar horario")
    print("6. Salir")

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
        print(numero_control)
    elif opcion == "2":
        print("\nSeleccionaste la opcion para registrar maestro\n")
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        rfc=input("Ingrese el RFC: ")
        sueldo=float(input("Ingrese el sueldo correspondiente: "))
        año= int(input("Ingrese el año de nacimiento: "))
        numero_control=escuela.generar_numero_control_maestro(nombre=nombre, rfc=rfc, año_nacimiento=año)

        maestro=Maestro(nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo, numero_control=numero_control)
        escuela.registrar_maestro(maestro=maestro)
        print(numero_control)
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("\nHasta pronto\n")
        break