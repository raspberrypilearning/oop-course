from turtle import Turtle
from random import randint

paul = Turtle()
paul.color('red')
paul.shape('turtle')
paul.penup()
paul.goto(-160, 100)
paul.pendown()

# Create three more instances of Turtle and make them race!
# Make sure each turtle starts slightly below the last so that they
# are not racing on top of each other

for movement in range(100):
    paul.forward(randint(1,5))