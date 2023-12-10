import turtle as t


class Snake:
    """Snake class is the definition of snake in My Snake Game"""

    def __init__(self):
        self.size = 3
        self.snake_body = []
        for i in range(self.size):
            new_snake_part = t.Turtle(shape="square")
            new_snake_part.color("white")
            new_xcor = 0 - 20 * i
            new_snake_part.goto(x=new_xcor, y=0)
            self.snake_body.append(new_snake_part)
