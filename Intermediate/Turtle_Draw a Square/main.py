from turtle import *

tim = Turtle()
tim.shape("turtle")
tim.color("DeepPink")

# Draw a square
for i in range(4):
    tim.fd(100)
    tim.right(90)

screen = Screen
exitonclick()
