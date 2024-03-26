from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def player_level(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("game over!", align="center", font=FONT)
