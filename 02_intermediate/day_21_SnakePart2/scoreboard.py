from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"
POSITION = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
