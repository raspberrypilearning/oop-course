from turtle import Turtle
from random import randint

john = Turtle()
john.color('red')
john.shape('turtle')
john.penup()
john.goto(-160, 100)
john.pendown()

# Create three more instances of Turtle and make them race!
# Make sure each turtle starts slightly below the last so that they
# are not racing on top of each other

for movement in range(100):
    john.forward(randint(1,5))

input("Press Enter to close")