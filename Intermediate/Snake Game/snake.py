from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.snake_head = self.blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_block = Turtle("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(position)
            self.blocks.append(new_block)

    def move(self):
        for block_num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            self.blocks[block_num].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def position_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)  # North

    def position_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)  # South

    def position_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)  # West

    def position_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)  # East



