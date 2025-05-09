#Random
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

# Setup the turtle
x = turtle.Turtle()
x.speed(0)  # Fastest drawing speed
x.pensize(3)  # Thicker lines
x.hideturtle()  # Hide turtle shape so only stars are visible

colorList = ["red", "green", "blue", "yellow", "purple"]

# Draw 100 stars at random positions
for i in range(100):
    x.penup()
    # Make sure the turtle is within visible range of the screen
    x.goto(random.randint(-350, 350), random.randint(-250, 250))
    x.pendown()

    # Set the color for the star
    x.color(colorList[i % len(colorList)])

    # Draw a 5-pointed star
    for _ in range(5):
        x.forward(50)  # Increased size of each star
        x.left(144)

    time.sleep(0.05)  # Small delay to see the star drawing

# Finish the drawing and hold the window open
turtle.done()