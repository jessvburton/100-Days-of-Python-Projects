from turtle import *
from random import randint


def change_colour():
    colormode(255)
    pencolor(randint(0, 255),
             randint(0, 255),
             randint(0, 255))


def draw_spirograph():
    circles = int(input("How many circles would you like?\n"))
    angle = 360 / circles
    for _ in range(circles):
        change_colour()
        circle(100)
        left(angle)


speed("fastest")
draw_spirograph()
exitonclick()
