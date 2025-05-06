#Floyd's Triangle
rows = int(input("Enter the number of rows for Floyd's Triangle:"))
startnum = 1

for i in range(rows+1):
    for j in range(i):
        print(startnum,end="")
        startnum +=1

    print()