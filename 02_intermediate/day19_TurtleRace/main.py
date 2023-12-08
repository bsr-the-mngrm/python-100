import turtle
import turtle as t
import random

is_race_on = False
turtles = []
colors = ["blue", "red", "yellow", "green", "purple"]

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race?\n{colors}\nEnter a color:")

for i in range(5):
    new_turtle = t.Turtle()
    new_turtle.color(colors[i])
    new_turtle.shape("turtle")
    new_turtle.penup()
    x = -230
    y = -100 + 30*i
    new_turtle.goto(x=x, y=y)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


screen.exitonclick()
