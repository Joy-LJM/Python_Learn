import time
from turtle import Turtle, Screen
from  snake import  Snake
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0) # to turn off animation

screen.listen() # listen to keystroke event
snake= Snake()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update() # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.1) # delay 1 second
    snake.move()








screen.exitonclick()