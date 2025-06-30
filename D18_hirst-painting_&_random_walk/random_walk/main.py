import turtle as t
import random

tim =t.Turtle()

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions=[0,90,180,270] # 0 - east 90 - north 180 - west 270 - south
tim.pensize(15)
tim.speed("fastest")

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color_tuple=(r,g,b) # tuple
    return random_color_tuple

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


