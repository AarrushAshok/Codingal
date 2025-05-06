#Half pyramid of numbers
num = int(input("Enter a number to display half pyramid of numbers:"))

for i in range(num):
    print(f"{i}","end=")
    for j in range(i):
        print("i", end="")
    print()