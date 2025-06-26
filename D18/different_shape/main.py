# import turtle as t

# timmy=t.Turtle()
# timmy.shape("turtle")
# timmy.color("green")
#
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

from turtle import Turtle, Screen
import random
t = Turtle()

# draw a dash line

# for _ in range(15):
#     t.forward(10)
#     t.color("white")
#     t.forward(10)
#     t.color("black")
# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
        angle = 360 / num_sides
        for _ in range(num_sides):
            t.forward(100)
            t.right(angle)
for side in range(3,11):
    t.color(random.choice(colours))
    draw_shape(side)
screen = Screen()
screen.exitonclick()
