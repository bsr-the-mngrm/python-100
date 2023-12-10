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
