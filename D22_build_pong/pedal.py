from turtle import Turtle, Screen


class Pedal(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
    def up(self):
        y_axis =self.ycor()+20
        self.goto(self.xcor(), y_axis)
    def down(self):
        y_axis =self.ycor()-20
        self.goto(self.xcor(), y_axis )