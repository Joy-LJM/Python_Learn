import turtle as t
tim=t.Turtle()
screen=t.Screen()

def go_forward():
    tim.forward(10)
def go_back():
    # tim.setheading(180)
    tim.backward(10)
def turn_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
    tim.forward(10)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
t.onkey(go_forward,"w")
t.onkey(go_back,"s")
t.onkey(turn_left,"a")
t.onkey(turn_right,"d")
t.onkey(clear_drawing,"c")
screen.exitonclick()