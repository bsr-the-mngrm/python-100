from turtle import Screen, bye
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    my_snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.update()

    screen.listen()
    screen.onkey(key="w", fun=my_snake.move_up)
    screen.onkey(key="a", fun=my_snake.move_left)
    screen.onkey(key="s", fun=my_snake.move_down)
    screen.onkey(key="d", fun=my_snake.move_right)
    screen.onkey(key="Escape", fun=scoreboard.game_over)

    while scoreboard.game_is_on:
        screen.update()
        time.sleep(0.10)

        if not my_snake.move_skip:
            my_snake.move()
        else:
            my_snake.move_skip = False

        # Detect collision with food
        if my_snake.head.distance(food) < 15:
            scoreboard.increase_score()
            my_snake.extend()
            food.refresh()

        # Detect collision with wall
        if (my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280
                or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280):
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in my_snake.snake_body[1:]:
            if my_snake.head.distance(segment) < 10:
                scoreboard.game_over()

    screen.onkey(key="Escape", fun=bye)
    screen.exitonclick()
