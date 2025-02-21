import colorgram
from turtle import *
import random


def extract_colors():
    """
    Extract x amount of colours from an image
    :return: list of colours. rgb in a tuple
    """
    colors = colorgram.extract('image.jpeg', 25)
    all_colors = []
    for c in range(len(colors)):
        rgb = (colors[c].rgb[0], colors[c].rgb[1], colors[c].rgb[2])
        all_colors.append(rgb)
    return all_colors


def draw_row_of_dots(dots, all_colors):
    """
    Draw 1 row of dots
    """
    for i in range(dots):
        dot(20, random.choice(all_colors))
        penup()
        forward(50)
        pendown()


def new_line(row_length):
    penup()
    left(90)
    forward(50)
    left(90)
    forward(row_length)
    right(180)


def create_dot_image():
    colormode(255)
    all_colors = extract_colors()

    dots = int(input("How many dots?"))
    row_length = dots * 50
    hideturtle()

    for i in range(dots):
        draw_row_of_dots(dots, all_colors)
        new_line(row_length)


create_dot_image()

screen = Screen
exitonclick()
