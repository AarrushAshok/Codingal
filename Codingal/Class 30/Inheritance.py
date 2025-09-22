#Inheritance
#Parent class - Vehicle
class Animal:
    def eat(self):
        print("Animal is eating.")

# Dog class that inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog is barking!")

# Cat class that inherits from Animal
class Cat(Animal):
    def meow(self):
        print("Cat says meow!")


# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

# Testing the methods
dog.eat()   # Inherited from Animal class
dog.bark()  # Unique to Dog class

cat.eat()   # Inherited from Animal class
cat.meow()  # Unique to Cat class
