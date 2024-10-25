"""
Написать класс Shape, который является родительским для класса Square,
который содержит конструктор, принимающий длину. Оба класса содержат метод
area() для расчета площади. Причем класс Shape имеет площадь равную нулю.
"""


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


shape = Shape()
print(f"Площадь фигуры: {shape.area()}")

square = Square(5)
print(f"Площадт квадрата: {square.area()}")
