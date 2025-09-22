#Dog Breed
class Dog:
    animal = "Dog"
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")

dog1 = Dog("Labrador", "Yellow")
dog2 = Dog("Bulldog", "White")
dog1.display_details()
dog2.display_details()