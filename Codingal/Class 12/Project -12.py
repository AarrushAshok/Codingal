#Half pyramid of numbers
num = int(input("Enter a number to display half pyramid of numbers:"))

for i in range(1,num+1):
    for j in range(i):
        print(f"{i}",end="")
    print()