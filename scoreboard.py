from turtle import Turtle


FONT = ("Times New Roman", 18, "normal")
ALIGNMENT = "left"
SCORE_POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.level = 1
        self.scoreboard()


    def scoreboard(self):
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over.", move=False, align="center", font=FONT)


