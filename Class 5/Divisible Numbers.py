#Divisible Numbers
number = int(input("Enter a number:"))
remainder = number %17
if remainder ==0 :
    print("It is divisible by 17")
else:
    print("It is not divisible by 17")