from turtle import Screen, bye
from paddle import Paddle, ComputerPaddle
from ball import Ball
import time

PLAYER_PADDLE_POSITION = (350, 0)
COMPUTER_PADDLE_POSITION = (-350, 0)

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    my_paddle = Paddle(PLAYER_PADDLE_POSITION)
    computer_paddle = ComputerPaddle(COMPUTER_PADDLE_POSITION)
    ball = Ball()

    screen.listen()
    screen.onkey(my_paddle.go_up, "Up")
    screen.onkey(my_paddle.go_down, "Down")
    screen.onkey(my_paddle.game_over, "Escape")

    while my_paddle.game_is_on:
        screen.update()
        time.sleep(0.1)

        ball.move()
        computer_paddle.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (ball.distance(my_paddle) < 50 and ball.xcor() > 320
                or ball.distance(computer_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

    screen.onkey(bye, "Escape")
    screen.exitonclick()
