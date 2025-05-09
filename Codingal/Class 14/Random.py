#Random
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

x = turtle.Turtle()
x.speed(0)
x.pensize(1)

colorList = ["red", "green", "blue", "yellow", "purple"]

for i in range(100):
    x.penup()
    x.goto(random.randint(-350, 350), random.randint(-250, 250))
    x.pendown()

    x.color(colorList[i % len(colorList)])

    for _ in range(5):
        x.forward(50)
        x.left(144)

turtle.done()