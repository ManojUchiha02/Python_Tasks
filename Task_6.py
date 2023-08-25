import math
class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self, base = None, height = None, equi_side = None):
        self.base = base
        self.height = height
        self.equi_side = equi_side

    def area(self):
        if self.base and self.height:
            return 0.5 * self.base * self.height
        elif self.equi_side:
            s = (self.equi_side + self.equi_side + self.equi_side) / 2
            return math.sqrt(s * (s - self.equi_side) * (s - self.equi_side) * (s - self.equi_side))
        else:
            return None
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Creating instances of the shapes
square = Square(int(input("Enter length of side of square:")))
triangle = Triangle(base = int(input("Enter base of triangle:")), height = int(input("Enter height of triangle:")))
triangle_equilateral = Triangle(equi_side = int(input("Side of equilateral triangle:")))
circle = Circle(int(input("Enter radius of circle:")))


# Calculating and printing areas
print("Area of Square:", square.area())
print("Area of Triangle:", triangle.area())
print("Area of Equilateral Triangle:", triangle_equilateral.area())
print("Area of Circle:", circle.area())
