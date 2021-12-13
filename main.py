#! python 3
#Day23.py
# this programme is based on Frogger

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('grey')

# player setup
player = Player()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

# scoreboard
scoreboard = Scoreboard()
scoreboard.update()

# car setup
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawn()
    car.move()
    # game finish
    if player.ycor() > 260:
        player.reset()
        scoreboard.next_level()
        car.next_level()
    # detect collision
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            player.reset()
            scoreboard.game_over()

screen.exitonclick()

