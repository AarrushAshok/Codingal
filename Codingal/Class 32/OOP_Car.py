#OOP
#class
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def drive(self):
        print(f"{self.year} {self.brand} {self.model} is now driving!")
    def brake(self):
        print(f"{self.year} {self.brand} {self.model} is slowing down.")

#objects
car1 = Car("Toyota", "Hyryder", 2002)
car2 = Car("Tesla", "Rocky", 2025)

car1.drive()
car1.brake()
car2.drive()
car2.brake()