from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def update_level(self):
        self.goto(STARTING_POSITION)

    def check_finish_line(self):
        return self.ycor() == FINISH_LINE_Y
