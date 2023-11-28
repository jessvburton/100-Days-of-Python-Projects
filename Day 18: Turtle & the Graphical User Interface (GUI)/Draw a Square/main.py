import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("DeepPink")

for i in range(4):
    tim.fd(100)
    tim.right(90)

screen = turtle.Screen
turtle.exitonclick()
