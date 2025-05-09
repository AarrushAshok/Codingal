#Calculating circumference using function
def calculateCircumference(radius):
    2 * 3.14 * radius

radius = float(input("Enter the radius of the circle:"))
circumference = calculateCircumference(radius)
print("The circumference of the circle is:",circumference)