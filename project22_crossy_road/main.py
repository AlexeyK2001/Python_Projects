import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
car = CarManager()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Crossy road")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.go_up, "Up")


game_is_on = True
scoreboard.update_level()
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create a new car
    car.create_cars()

    # move cars
    car.move()

    # Detect collission with a car
    for i in car.cars:
        if player.distance(i) < 25:
            scoreboard.game_over()
            player.stop_by_hitting()
            game_is_on = False

    # Detect crossing
    if player.ycor() >= 280:
        player.finish()
        car.increase_speed()
        scoreboard.update_level()

screen.exitonclick()
