from turtle import Turtle
import random

class Food(Turtle):

    # Generate piece of food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
        