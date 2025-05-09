#Random
x = turtle.Turtle()
x.speed(0)
colorList = ["red","green","blue","yellow","purple"]

for i in range(100):
    x.penup()
    x.goto(random.randint(-100,100,random.randint(-300,300)))
    x.pendown()

for i in range(5):
    x.color(colorList[i%5])
    x.forward(i+10)
    x.left(144)