from turtle import Turtle

INITIAL_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_bit = Turtle("square")
            new_bit.color("white")
            new_bit.penup()
            new_bit.goto(position)
            self.snake_body.append(new_bit)

    def move(self):

        # Last bit takes the place of preceding bit untill the head assumes new position
        for bit_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[bit_num - 1].xcor()
            new_y = self.snake_body[bit_num - 1].ycor()
            self.snake_body[bit_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)