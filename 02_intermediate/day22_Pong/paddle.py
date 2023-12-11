from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class ComputerPaddle(Paddle):

    def __init__(self, position: tuple[float, float]):
        super().__init__(position)
        self.y_move = 20

    def move(self):
        if self.y_move < 0 and self.ycor() < -200:
            self.y_move *= -1
        elif self.y_move > 0 and self.ycor() > 200:
            self.y_move *= -1

        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
