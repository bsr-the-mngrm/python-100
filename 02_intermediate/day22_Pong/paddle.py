from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position: tuple[float, float]):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=20, stretch_len=100, outline=None)
        self.penup()
        self.goto(position)
        