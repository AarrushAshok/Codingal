#Factorial
num = int(input("Enter a positive number:"))
factorial = 1

if num <0:
    print("Factorial is not defined for negative numbers")
else:
    for num in range (1,num+1):
        factorial *= num

print(f"Factorial of {num} is : {factorial}")