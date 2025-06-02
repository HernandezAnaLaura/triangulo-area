class Triangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0

    def leer_datos(self):
        self.base = float(input("Ingresa la base: "))
        self.altura = float(input("Ingresa la altura: "))

    def calcular_area(self):
        return (self.base * self.altura) / 2

t = Triangulo()         
t.leer_datos()         
print("el area es:", t.calcular_area()) 