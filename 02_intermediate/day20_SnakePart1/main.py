import turtle as t
import snake as s

if __name__ == '__main__':
    screen = t.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")

    my_snake = s.Snake()

    screen.exitonclick()
