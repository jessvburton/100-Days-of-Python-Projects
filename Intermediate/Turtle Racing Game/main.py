from turtle import Turtle, Screen
import random

race_turtles = {
    "red": -150,
    "orange": -90,
    "yellow": -30,
    "green": 30,
    "blue": 90,
    "purple": 150
}
ready_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

for colour, y_position in race_turtles.items():
    turtle_name = Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(colour)
    turtle_name.goto(x=-230, y=y_position)
    ready_turtles.append(turtle_name)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in ready_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
