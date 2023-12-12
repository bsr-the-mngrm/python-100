from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        for _ in range(28):
            new_car = Car()
            self.cars.append(new_car)

    def moving_cars(self):
        for car in self.cars:
            if car.xcor() > -320:
                car.move()
            else:
                car.setup_position()


class Car(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setup_position()
        self.move_distance = STARTING_MOVE_DISTANCE

    def setup_position(self):
        new_x = random.randint(320, 400)
        new_y = random.randint(-270, 270)
        self.goto(new_x, new_y)

    def move(self):
        new_x = self.xcor() + self.move_distance
        self.goto(new_x, self.ycor())

    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT
