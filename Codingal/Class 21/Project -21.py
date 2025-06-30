#Filtering square numbers
list = []

lowerNumberInRange = int(input("Enter the lower range:"))
upperNumberInRange = int(input("Enter the upper range:"))

for x in range(lowerNumberInRange,upperNumberInRange+1):
    sqr = x**2
    list.append(sqr)

oddSquares = []
evenSquares = []

for x in list:
    if x%2==0:
        evenSquares.append(x)
    else:
        oddSquares.append(x)

print("Odd Squares:",oddSquares)
print("Even Squares:",evenSquares)