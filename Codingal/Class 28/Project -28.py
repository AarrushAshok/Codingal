#Area and Perimeter of a Circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius #Formula for area: pi * (r)square   
    def perimeter(self):
        return 2 * math.pi * self.radius #Formula for perimeter: 2 * pi * r

radius = float(input("Enter the radius of the circle: "))
my_circle = Circle(radius)

print("Area of the circle:",my_circle.area())
print("Perimeter of the circle:",my_circle.perimeter())