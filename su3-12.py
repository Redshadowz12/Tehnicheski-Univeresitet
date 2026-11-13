import math


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print("Area: ", self.width * self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Area: {math.pi * self.radius ** 2:.2f}")

rect = Rectangle(5, 10)
circ = Circle(4)
rect.area()
circ.area()