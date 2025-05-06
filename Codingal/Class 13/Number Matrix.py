#Number Matrix
num = int(input("Enter a number: "))
startnum =1

for i in range(num):
    for j in range(num):
        print(startnum,end="" )
        startnum +=1
    
    print()