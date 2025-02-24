from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# # loading screen / start screen
# loading_screen = True
# while loading_screen:
#     ready = input("Are you ready to start? (y/n): ").lower()
#
#     if ready == 'y' or ready == 'yes':
#         loading_screen = False


snake = Snake()

screen.listen()
screen.onkey(snake.position_up,"Up")
screen.onkey(snake.position_down, "Down")
screen.onkey(snake.position_left, "Left")
screen.onkey(snake.position_right, "Right")


start_game = True
while start_game:
    screen.update()
    time.sleep(0.1)

    snake.move()


    screen.exitonclick()






# TODO: Detect collision with food
# TODO: Create scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail





# screen.exitonclick()
