import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class is the definition of snake in My Snake Game"""

    def __init__(self):
        self.game_is_on = True
        self.snake_body = []
        self.__create_snake()
        self.head = self.snake_body[0]

    def __create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake_part = t.Turtle(shape="square")
            new_snake_part.color("white")
            new_snake_part.penup()
            new_snake_part.goto(position)
            self.snake_body.append(new_snake_part)

    def move(self):
        """Move snake body parts"""
        for body_part_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_part_num-1].xcor()
            new_y = self.snake_body[body_part_num-1].ycor()
            self.snake_body[body_part_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """Move snake forward"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

        self.move()

    def move_down(self):
        """Move snake forward"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        self.move()

    def move_right(self):
        """Turn snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self.move()

    def move_left(self):
        """Turn snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self.move()

    def stop_game(self):
        self.game_is_on = False
