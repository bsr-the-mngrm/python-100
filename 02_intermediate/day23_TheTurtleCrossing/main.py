import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.moving_cars()

    if player.check_finish_line():
        scoreboard.update_level()
        player.update_level()
        car_manager.update_level()

    # Detect Turtle and Car collision
    if car_manager.check_collision(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
