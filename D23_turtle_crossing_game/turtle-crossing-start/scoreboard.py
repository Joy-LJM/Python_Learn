from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 0
        self.hideturtle()
        self.update_score()
        self.level=1
    def update_score(self):
        self.goto(0,260)
        self.write(f"Score: {self.level}", align="center", font=FONT)
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
