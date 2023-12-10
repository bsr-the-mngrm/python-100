import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """Snake class is the definition of snake in My Snake Game"""

    def __init__(self):
        self.game_is_on = True
        self.snake_body = []
        for position in STARTING_POSITIONS:
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

    def move_up(self):
        """Move snake forward"""
        self.__move()
        self.snake_body[0].setheading(90)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_down(self):
        """Move snake forward"""
        self.__move()
        self.snake_body[0].setheading(270)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_right(self):
        """Turn snake right"""
        self.__move()
        self.snake_body[0].setheading(0)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_left(self):
        """Turn snake left"""
        self.__move()
        self.snake_body[0].setheading(180)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def stop_game(self):
        self.game_is_on = False
