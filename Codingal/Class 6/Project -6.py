#Basic Calculator
print("Welcome to Basic Calculator!")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number of the operation (1/2/3/4): ")

if choice == '1':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print("The result of addition is:", result)

elif choice == '2':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 - num2
    print("The result of subtraction is:", result)

elif choice == '3':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    print("The result of multiplication is:", result)

elif choice == '4':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
    else:
        print("Division by zero cannot be done")

else:
    print("Invalid choice")