from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FONT2 = ("Courier", 12, "normal")
COLOR = "white"
POSITION = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.score = 0
        self.high_score = self.load_highscore()

        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\tHigh score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def write_highscore(self, score):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def game_over(self):
        self.game_is_on = False
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write("(press 'Esc' to exit)", align=ALIGNMENT, font=FONT2)

    @staticmethod
    def load_highscore():
        with open("data.txt") as file:
            return int(file.read())
