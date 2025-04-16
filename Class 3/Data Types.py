w = 10 #int
x = 20.5 #float
y = "Hello World!" #string
z = True #Boolean: True, False

print("value of w is:",w)
print("type of data stored in w is:",type(w))

print("value of x is:",x)
print("type of data stored in x is:",type(x))

print("value of y is:",y)
print("type of data stored in y is:",type(y))

print("value of z is:",z)
print("type of data stored in z is:",type(z))

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

print("Addition of two numbers is",num1+num2)
print("Subtraction of two numbers is",num1-num2)
print("Product of two numbers is",num1*num2)
print("Division of two numbers is",num1/num2)
print("Power of number1 on number 2 is",num1**num2)

MathematicsMark = 90
BiologyMark = 97
ChemistryMark = 95
EconomicsMark = 100
PhysicsMark = 89

PercentageMark = (MathematicsMark+BiologyMark+ChemistryMark+EconomicsMark+PhysicsMark)/500*100
TotalMark = (MathematicsMark+BiologyMark+ChemistryMark+EconomicsMark+PhysicsMark)
print("TotalMark",TotalMark)
print("PercentageMark",PercentageMark,"%")