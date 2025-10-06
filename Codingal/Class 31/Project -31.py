#Vehicle Polymorphism
class Car:
    def __init__(self, brand, fuel_type, max_speed):
        self.brand = brand
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        print(f"{self.brand} car created!")
    def displayInfo(self):
        print(f"Brand: {self.brand}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Max Speed: {self.max_speed}")

class BMW(Car):
    def __init__(self):
        super().__init__("BMW", "Petrol", "250 km/h")

class Ferrari(Car):
    def __init__(self):
        super().__init__("Ferrari", "Petrol", "350 km/h")

bmw = BMW()
ferrari = Ferrari()
bmw.displayInfo()
ferrari.displayInfo()