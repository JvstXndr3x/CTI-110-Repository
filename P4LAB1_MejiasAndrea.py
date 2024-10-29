# Andrea Mejias
# 10/29/2024
# P4LAB1
# Use loops and turtle library to draw a house.

# Import the turtle library
import turtle

# Set up window and turtle object
window = turtle.Screen()
tessa = turtle.Turtle()

# Add features to object
tessa.pensize(10)
tessa.pencolor("purple")
tessa.shape("arrow")

# While loop that runs four times
movement = 0

while movement <= 3:
    movement += 1
    tessa.forward(100)
    tessa.right(90)

# For loop that runs three times
for side in range (3):
    tessa.forward(100)
    tessa.left(120)
