from turtle import Screen, Turtle
from ball import Ball
import time
from scoreboard import Scoreboard
import random
from pedal import Pedal
screen = Screen()
scoreboard = Scoreboard()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

turtle = Turtle()
turtle.color("white")
turtle.shape("square")
turtle.shapesize(stretch_wid=0.5, stretch_len=0.1)
turtle.pendown()

screen.listen()

r_paddle = Pedal((-380, 0))
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

l_paddle=Pedal((380, 0))
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
ball=Ball()

game_is_on=True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    #detect hit the wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
        # detect collision with r_paddle: hit the center,斜斜hit
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.xcor() < -320 and ball.distance(l_paddle) <50:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.increase_l_score()
    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.increase_r_score()

screen.exitonclick()