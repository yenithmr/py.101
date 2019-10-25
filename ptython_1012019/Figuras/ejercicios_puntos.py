from figuras import *
p1 = Punto(0,5)
p2 = Punto(5,10)

cuadrado = Cuadrado(p1,p2)
circulo = Circulo(p1,p2)
rectangulo = Rectangulo(p1,p2)
triangulo = Triangulo(p1,p2)

cuadrado.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_area()
circulo.calcular_perimetro()
rectangulo.calcular_area()
rectangulo.calcular_perimetro()

triangulo.calcular_area()
triangulo.calcular_perimetro()


print (cuadrado.area)
print (cuadrado.perimetro)
print (circulo.area)
print (circulo.perimetro)
print (rectangulo.area)
print (rectangulo.perimetro)
print (triangulo.area)
print (triangulo.perimetro)
