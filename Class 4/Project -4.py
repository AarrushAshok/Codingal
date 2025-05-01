#Square Root
import math
number = int(input("Enter a number to find its square root:"))
if number < 0:
    print("Square root of negative number is not possible")
else:
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")