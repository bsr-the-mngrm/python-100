from turtle import Turtle

STEP_DISTANCE = 50


class Ball(Turtle):
    
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
