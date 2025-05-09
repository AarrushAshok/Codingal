#Hexagon using turtle
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

x = turtle.Turtle()
x.speed(0)
x.pensize(2)

for i in range(5):
    x.penup()
    x.goto(random.randit(-300,300),random.randint(-300,300))
    x.pendown()

for i in range(6):
    x.forward(50)
    x.left(60)

turtle.done()