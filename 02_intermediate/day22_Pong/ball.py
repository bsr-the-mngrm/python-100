from turtle import Turtle

UP_RIGHT = 45
UP_LEFT = 135
DOWN_LEFT = 225
DOWN_RIGHT = 315

TOP_WALL = 270
BOTTOM_WALL = -270
RIGHT_WALL = 370
LEFT_WALL = -370

STEP_DISTANCE = 50


class Ball(Turtle):
    
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.penup()
        self.setheading(DOWN_LEFT)

    def __check_wall_collisions(self):
        if self.ycor() > TOP_WALL:
            if self.heading() == UP_RIGHT:
                self.setheading(DOWN_RIGHT)
            else:
                self.setheading(DOWN_LEFT)
        elif self.ycor() < BOTTOM_WALL:
            if self.heading() == DOWN_RIGHT:
                self.setheading(UP_RIGHT)
            else:
                self.setheading(UP_LEFT)

        if self.xcor() > RIGHT_WALL:
            if self.heading() == UP_RIGHT:
                self.setheading(UP_LEFT)
            else:
                self.setheading(DOWN_LEFT)
        elif self.xcor() < LEFT_WALL:
            if self.heading() == UP_LEFT:
                self.setheading(UP_RIGHT)
            else:
                self.setheading(DOWN_RIGHT)

    def move(self):
        self.__check_wall_collisions()
        self.forward(STEP_DISTANCE)
