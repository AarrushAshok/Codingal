#Inheritance (Parent -----> Child)
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