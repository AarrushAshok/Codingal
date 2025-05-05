#Descending Order of Numbers
n1 = int(input("Enter 1st Number:"))
n2 = int(input("Enter 2nd Number:"))
n3 = int(input("Enter 3rd Number:"))
n4 = int(input("Enter 4th Number:"))
n5 = int(input("Enter 5th Number:"))

#Assumption of n1 being the Highest number
#Assumption of n2 being the Second highest number
HighestNumber = n1
SecondHighestNumber = n2

if n2>HighestNumber:
    HighestNumber = n2
    SecondHighestNumber = n1
if n3>HighestNumber:
    HighestNumber = n3
    SecondHighestNumber = HighestNumber
elif n3>SecondHighestNumber:
    SecondHighestNumber = n3
if n4>HighestNumber:
    HighestNumber = n4
    SecondHighestNumber = HighestNumber
elif n4>SecondHighestNumber:
    SecondHighestNumber = n4
if n5>HighestNumber:
    HighestNumber = n5
    SecondHighestNumber = HighestNumber
elif n5>SecondHighestNumber:
    SecondHighestNumber = n5

print("Highest number is:",HighestNumber)
print("Second highest number is:",SecondHighestNumber)