#Recursion
def f1(num):
    if num == 0: return
    print("this is f1,num:",num)
    f1(num-1)

f1(5)