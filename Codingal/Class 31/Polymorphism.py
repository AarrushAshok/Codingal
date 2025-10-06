#Polymorphism in a Office
#Polymorphism is called Overriding used by a function called "super"

class CEO:
    def __init__(self, nm, id, sal):
        self.name = nm
        self.id = id
        self.baseSal = sal
        print(self.name, "joined today")
    def displayInfo(self):
        print(f"name: {self.name}\nId: {self.id}\nBase Salary: {self.baseSal}")

class MD(CEO):
    def __init__(self, nm, id, sal, dpt):
        self.department = dpt
        super().__init__(nm, id, sal)
    def displayInfo(self):
        super().displayInfo()
        print(f"Department: {self.department}")

class Developer(CEO):
    def __init__(self, nm, id, sal,dpt):
        self.department = dpt
        super().__init__(nm, id, sal)
    def displayInfo(self):
        super().displayInfo()
        print(f"Department: {self.department}")

Aarush = CEO("Aarush", "ceo001", 90000)
Raj = CEO("Raj", "ceo002", 90000)
Sam = MD("Sam", "md001", 900000, "Python Department")
Alex = Developer("Alex", "dev001", 120000,"Expertise")

Aarush.displayInfo()
Raj.displayInfo()
Sam.displayInfo()
Alex.displayInfo()