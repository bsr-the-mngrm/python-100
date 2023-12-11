from turtle import Screen, bye
from paddle import Paddle, ComputerPaddle
import time

PLAYER_PADDLE_POSITION = (350, 0)
COMPUTER_PADDLE_POSITION = (-350, 0)

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")

    my_paddle = Paddle(PLAYER_PADDLE_POSITION)
    computer_paddle = ComputerPaddle(COMPUTER_PADDLE_POSITION)

    screen.tracer(0)

    screen.listen()
    screen.onkey(my_paddle.go_up, "Up")
    screen.onkey(my_paddle.go_down, "Down")
    screen.onkey(my_paddle.game_over, "Escape")

    while my_paddle.game_is_on:
        screen.update()
        time.sleep(0.1)

        computer_paddle.move()

    screen.onkey(bye, "Escape")
    screen.exitonclick()
