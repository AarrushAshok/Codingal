#Random Module
import random
import turtle

arrow = turtle.Turtle()
arrow.speed(0)
arrow.pencolor("red")
for y in range(100):
    for x in range(5):
        arrow.forward(30)
        arrow.right(144)
    a = random.randint(-450,450)
    b = random.randint(-450,450)
    arrow.penup()
    arrow.goto(a,b)
    arrow.pendown()
turtle.done


x = random.randint(1,20)
name = "Sam"
list1 = [1,2,3,4,5,"Aarush",True,False,45.7]
randomChar = random.choice(name)
randomFromList1 = random.choice(list1)
print("Value of x is:",x)
print("Random character is:",randomChar)
print("Random from list is:",randomFromList1)