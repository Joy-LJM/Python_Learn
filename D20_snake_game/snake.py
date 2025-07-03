
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head=self.segment_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
          self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)
    def extend_segment(self):
        self.add_segment(self.segment_list[-1].position())# add to the last position

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):  # range(start,stop,range) range=-1 : reverse the order
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.segment_list[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT: # can not go back
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

