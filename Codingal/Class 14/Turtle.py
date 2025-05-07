#Turtle
import turtle

x = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#172030")

x.speed(0)
x.pencolor("orange")
x.pensize(3)

ColorList = ["red","green","blue","brown","yellow"]

for i in range(4):
    x.color(ColorList[i%5])
    x.forward(100)
    x.left(90)

x.penup()
x.goto(-100,100)
x.pendown()

for i in range(100):
    x.color(ColorList[i%5])
    x.forward(i+10)
    x.left(144)

turtle.done()