from turtle import *
from random import randint

colormode(255)
shapes = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8, "nonagon": 9,
          "decagon": 10}


def change_colour():
    pencolor(randint(0, 255),
             randint(0, 255),
             randint(0, 255))


for i in shapes:
    change_colour()
    for _ in range(shapes[i]):
        forward(100)
        right(360/shapes[i])


screen = Screen
exitonclick()
