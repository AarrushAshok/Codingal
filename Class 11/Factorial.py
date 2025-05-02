#Factorial
num = int(input("Enter a positive number:"))
if num <0:
    print("Factorial is not defined for negative numbers")
else:
    for num in range (1,21):
        factorial = 1
        print(f"Factorial of {num} is : {factorial}")