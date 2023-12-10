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

    def __move(self):
        """Move snake body parts"""
        for body_part_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_part_num-1].xcor()
            new_y = self.snake_body[body_part_num-1].ycor()
            self.snake_body[body_part_num].goto(x=new_x, y=new_y)

    def move_forward(self):
        """Move snake forward"""
        self.__move()
        self.snake_body[0].forward(20)

    def move_right(self):
        """Turn snake right"""
        self.__move()
        self.snake_body[0].right(90)
        self.snake_body[0].forward(20)


    def move_left(self):
        """Turn snake left"""
        self.__move()
        self.snake_body[0].left(90)
        self.snake_body[0].forward(20)
