class Coche:
    marca = ""
    modelo = ""
    año = 0

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_info(self):
        print("Marca del coche: ", self.marca)
        print("Modelo del coche: ", self.modelo)
        print("Año del coche: ", self.año)

    def calcular_edad_coche(self):
        print("Edad del coche: ", 2024-self.año)