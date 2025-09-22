#Inheritance
#Parent -----> Child is called inheritance
# Parent class also called as Super class
#Child class also called as Sub class
#When constructor called ------> Object is created
class Parent:
    x =10
    def f1(self):
        print("f1 from class A")
#Child has become child class of parent class
class Child(Parent):
    pass

#Objects
a = Parent()
b = Child()
print(a.x)
a.f1()
print(b.x)
b.f1()

class Vehicle:
    def __init__(self):
        print("Vehicle(parent)class constructor is called")
    def move(self):
        print("vehicle is moving")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car(child of Vehicle)constructor is called")
    def honk(self):
        print("car goes honk")

c1 = Car()
c1.honk()
c1.move()



class Vehicle:
    def __init__(self):
        print("Vehicle is started(constructor called)")
    def move(self):
        print("Vehicle is started")

class Bike(Vehicle):
    def kick_start(self):
        print("Bike kick-started!")

b1 =Bike()
b1.move()