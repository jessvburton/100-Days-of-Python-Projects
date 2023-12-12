from turtle import *
from random import *

pensize(10)
speed("fast")
colormode(255)
directions = [0, 90, 180, 270]


def change_colour():
    pencolor(randint(0, 255),
             randint(0, 255),
             randint(0, 255))


while True:
    change_colour()
    forward(50)
    setheading(choice(directions))
