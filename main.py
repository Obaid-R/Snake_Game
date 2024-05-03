from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0) # Turns off the delay in the turtle animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect when head of the snake comes in contact with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect when head of the snake comes in contact with a wall
    if (snake.head.xcor() > 295 or snake.head.xcor() < -295) or (snake.head.ycor() > 295 or snake.head.ycor() < -295):
        scoreboard.reset()
        snake.reset_snake()

    # Detect when head of the snake comes in contact with the snake body (with the exception of the head itself)
    for bit in snake.snake_body[1:-1]:
        if snake.head.distance(bit) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
