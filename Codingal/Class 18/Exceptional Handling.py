#Exception
x = 0 #(default value)
try:
    x = int(input("Enter a number:"))
except ValueError as ve: #(catch)
    print("Invalid Input.Please enter a valid number")

print("Processing")
print("Processing")
print("Processing")
print("Processing")
print("Processing")
print("Value of x is:",x)

