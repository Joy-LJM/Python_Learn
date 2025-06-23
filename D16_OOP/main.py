from turtle import *
from prettytable import PrettyTable

# tim=Turtle()#Turtle class
# tim.shape("turtle")
# tim.color("green")
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.speed("slow")
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick() #method

table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align="l"

print(table)