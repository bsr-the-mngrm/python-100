from turtle import Turtle

UP = 90
DOWN = 270
STEP_DISTANCE = 50


class Paddle(Turtle):

    def __init__(self, position: tuple[float, float]):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        self.penup()
        self.goto(position)
        self.setheading(UP)

        self.game_is_on = True

    def go_up(self):
        self.setheading(UP)
        self.forward(STEP_DISTANCE)

    def go_down(self):
        self.setheading(DOWN)
        self.forward(STEP_DISTANCE)

    def game_over(self):
        self.game_is_on = False
