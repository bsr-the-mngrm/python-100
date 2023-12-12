from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-210, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(LEVEL_POSITION)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
