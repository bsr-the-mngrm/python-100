import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)

colors = colorgram.extract('image.jpg',25)

print(colors)
#
# screen = t.Screen()
# screen.exitonclick()
