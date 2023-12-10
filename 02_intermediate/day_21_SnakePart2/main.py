from turtle import Screen
from snake import Snake
from food import Food
import time


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    my_snake = Snake()
    food = Food()

    screen.update()

    screen.listen()
    screen.onkey(key="w", fun=my_snake.move_up)
    screen.onkey(key="a", fun=my_snake.move_left)
    screen.onkey(key="s", fun=my_snake.move_down)
    screen.onkey(key="d", fun=my_snake.move_right)
    screen.onkey(key="Escape", fun=my_snake.stop_game)

    while my_snake.game_is_on:
        screen.update()
        time.sleep(0.1)

        my_snake.move()
