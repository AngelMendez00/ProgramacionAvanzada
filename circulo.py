class Circulo:
    radio=0

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
            print("\nCirculo de radio: ", self.radio)
            print("Area: ", pow(self.radio,2)*3.1416)

    def calcular_perimetro(self):
            print("\nCirculo de radio: ", self.radio)
            print("Perimetro: ", self.radio*2*3.1416)