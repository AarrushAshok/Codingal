#Multiplication Table
print("Multiplication Table:")
number = int(input("Enter a number:"))
for x in range(1,21):
    result = number * x
    print(f"{number}*{x} = {result}")