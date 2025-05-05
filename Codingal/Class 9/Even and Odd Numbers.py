#Even and Odd Numbers
num = int(input("Enter a number:"))
if num > 0:
    if num % 2 ==0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is negative. Unable to find if the number is odd or even")