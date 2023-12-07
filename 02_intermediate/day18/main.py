import turtle as t
import random

tim = t.Turtle()

turtle_colors = ["azure", "lime green", "forest green", "olive", "gold", "wheat", "firebrick", "deep pink", "purple",
                 "blue violet", "lavender", "slate blue", "gray", "deep sky blue", "sienna"]

directions = [0, 90, 180, 270]

tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(turtle_colors))
    tim.setheading(random.choice(directions))
    tim.forward(20)

screen = t.Screen()
screen.exitonclick()
