from turtle import Screen
from snake import Snake
import time

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0) # Turns off the delay in the turtle animation

snake = Snake()

# Read in input from the keyboard to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

program_running = True
while program_running:
    screen.update()
    time.sleep(0.06) #Add a 0.06 second delay everytime snake_body moves

    snake.move()









screen.exitonclick()
