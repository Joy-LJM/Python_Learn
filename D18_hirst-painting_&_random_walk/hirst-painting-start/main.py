###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

tim=t.Turtle()
tim.speed("fastest")
t.colormode(255) #Set pencolor to the RGB color represented by the tuple
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100


for i in range(1, number_of_dots+1):

        tim.dot(20, random.choice(rgb_colors))
        tim.fd(50)
        if i%10==0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

t.Screen().exitonclick()

print(rgb_colors)