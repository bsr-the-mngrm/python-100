import turtle as t
import snake as s
import time

if __name__ == '__main__':
    screen = t.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    my_snake = s.Snake()

    screen.update()

    game_is_on = True

    while game_is_on:
        my_snake.move_forward()
        time.sleep(0.2)
        screen.update()

    screen.exitonclick()
