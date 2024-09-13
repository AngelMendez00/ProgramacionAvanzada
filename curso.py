class Curso:
    nombre_curso=""
    codigo_curso=""
    instructor=""

    def __init__(self, nombre, codigo, instructor):
        self.nombre_curso=nombre
        self.codigo_curso=codigo
        self.instructor=instructor

    
    def mostrar_info_curso(self):
        print("\n---------Info de curso-----------\n")
        print("Codigo:", self.codigo_curso)
        print("Curso:", self.nombre_curso)
        print("Instructor:", self.instructor)