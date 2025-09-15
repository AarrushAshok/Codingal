# Object-Oriented Programming (OOP)
# A class is the blueprint for creating an abject.
# Here, the class "Human" serves as a blueprint for creating individual human objects.

class Human:
    # 1. Constructor (__init__ method)
    # 2. Properties/Characteristics (variables)
    # 3. Functionalities/Behavior (methods)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"Constructor of Human class is called for {self.name}")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Creating objects from the Human class
aarush = Human("Aarush Ashok", 14, "Male")
john = Human("John Doe", 30, "Male")
sam = Human("Sam Smith", 25, "Female")

# Demonstrating functionality by calling methods on the objects
aarush.eat()
john.sleep()
sam.eat()