class Estudiante:
    nombre=""
    edad=0
    id_estudiante=0
    cursos=[]

    def __init__(self, nombre, edad, id_estudinte, ):
        self.nombre=nombre
        self.edad=edad
        self.id_estudiante=id_estudinte
        self.cursos=[]

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_informacion(self):
        print("\n---------Estudiante-----------\n")
        print("Nombre del estudiante: ", self.nombre)
        print("Edad del estudiante: ", self.edad)
        print("ID del estudiante: ", self.id_estudiante)
        print("Cursos del estudiante")
        if len(self.cursos)==0:
            print("Estudiante sin cursos aun\n")
        else:
            for curso in self.cursos:
                print("Curso: ", curso.nombre_curso)
