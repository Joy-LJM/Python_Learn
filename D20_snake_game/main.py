import time
from turtle import Screen
from  snake import  Snake
from food import Food
from scoreboard import Scoreboard

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

food = Food()
scoreboard = Scoreboard()

game_is_on=True
while game_is_on:
    screen.update() # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.1) # delay 1 second
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15: # check the distance between the first square of snake and food
        food.refresh()
        scoreboard.increase_score()
        snake.extend_segment()

    # detect hit the wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on=False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segment_list[1:]:
        # skip the first one: can slice the first one as above[1:]
        # if segment == snake.head:
        #     pass
        #elif
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()