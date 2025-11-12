#OOP
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def study(self):
        print(f"{self.name} is studying {self.subject}.")
    def introduce(self):
        print(f"I'm {self.name} studying in grade {self.grade} and i love to study {self.subject}.")

student1 = Student("Rita", "10", "Maths")
student2 = Student("Sam", "11", "Social")
student3 = Student("Aarush", "12", "Economics")

student1.introduce()
student1.study()
student2.introduce()
student2.study()
student3.introduce()
student3.study()