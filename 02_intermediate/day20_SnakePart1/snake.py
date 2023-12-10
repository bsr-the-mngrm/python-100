import turtle as t


class Snake:
    """Snake class is the definition of snake in My Snake Game"""

    starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.snake_body = []
        for position in Snake.starting_positions:
            new_snake_part = t.Turtle(shape="square")
            new_snake_part.color("white")
            new_snake_part.penup()
            new_snake_part.goto(position)
            self.snake_body.append(new_snake_part)

    def move_forward(self):
        """Move snake forward"""
        for body_part in self.snake_body:
            body_part.forward(20)

    def move_right(self):
        """Turn snake right"""
        pass

    def move_left(self):
        """Turn snake left"""
        pass
