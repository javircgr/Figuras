class Figura():
    def __init__(self):
        pass

    def calcular_area():
        pass

    def calcular_perimetro():
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = self.lado ** 2
        return area

    def calcular_perimetro(self):
        perimetro = self.lado * 4
        return perimetro

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = (2 * self.base) + (2 * self.altura)
        return perimetro


c = Cuadrado(2)
print('El area del cuadrado es',c.calcular_area())
print('El perimetro del cuadrado es',c.calcular_perimetro())

r = Rectangulo(2,3)
print('El area del rectangulo es',r.calcular_area())
print('El perimetro del rectangulo es',r.calcular_perimetro())
