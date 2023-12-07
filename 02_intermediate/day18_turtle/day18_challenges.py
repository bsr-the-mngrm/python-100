import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# # Challenge 4

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
# # turtle_colors = ["azure", "lime green", "forest green", "olive", "gold", "wheat", "firebrick", "deep pink",
# #                  "purple", "blue violet", "lavender", "slate blue", "gray", "deep sky blue", "sienna"]


# directions = [0, 90, 180, 270]
#
# tim.pensize(5)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(20)

# Challenge 5

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim.pensize(5)
tim.speed("fastest")
draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()
