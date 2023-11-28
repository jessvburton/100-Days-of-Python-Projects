from turtle import *

tim = Turtle()
tim.shape("turtle")

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen
exitonclick()
