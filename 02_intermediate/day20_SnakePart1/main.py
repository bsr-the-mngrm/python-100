import turtle as t
import snake as s

if __name__ == '__main__':
    screen = t.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")

    my_snake = s.Snake()

    game_is_on = True

    while game_is_on:
        for body_part in my_snake.snake_body:
            body_part.forward(20)

    screen.exitonclick()
