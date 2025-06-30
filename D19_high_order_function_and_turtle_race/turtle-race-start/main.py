from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="What is your bet?")
colors = ["red", "orange", "yellow", "violet", "purple"]
turtle_list = []
y_axile = -100
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y_axile)
    y_axile += 40
    turtle_list.append(new_turtle)
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winner is {winning_color} turtle")
            else:
                print(f"You lost! The winner is {winning_color} turtle")
        turtle.forward(random.randint(1, 10))

screen.exitonclick()
