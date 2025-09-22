#Private Attributes
#To make a variable private, give 2 underscores infront of the variable
class FabricsEmployee:
    __CEO = "Aarush" #Is now private after adding 2 underscores
    def __init__(self,nameValue):
        self.name = nameValue
    def displayInfo(self):
        print(f"name of Employee is: {self.name}")
        print(f"name of CEO is: {self.__CEO}")

John = FabricsEmployee("John")
Marc = FabricsEmployee("Marc")
Sam = FabricsEmployee("Sam")

John.displayInfo()
Marc.displayInfo()
Sam.displayInfo()

John.__CEO = "Marc"
John.displayInfo()