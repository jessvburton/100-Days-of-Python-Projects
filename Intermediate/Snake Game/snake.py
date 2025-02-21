from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()

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

        self.blocks[0].forward(MOVE_DISTANCE)


















