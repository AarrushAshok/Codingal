#Hexagon using turtle
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

x = turtle.Turtle()
x.speed(0)
x.pensize(2)

colorList = ["red", "green", "blue", "yellow", "purple"]

for i in range(5):
    x.penup()
    x.goto(-200 + (i * 100), 0)
    x.pendown()

    x.color(colorList[i % len(colorList)])


    for i in range(6):
        x.forward(50)
        x.left(60)

turtle.done()