#Exception
x = 0 #(default value)
try:
    x = int(input("Enter a number:"))
except ValueError as ve: #(catch)
    print("Invalid Input.Please enter a valid number")
except ZeroDivisionError as zde :
    print("Can't Divide a number by 0")

print("Processing")
print("Processing")
print("Processing")
print("Processing")
print("Processing")
print("Value of x is:",x)

