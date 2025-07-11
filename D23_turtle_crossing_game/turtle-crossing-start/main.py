import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle_player=Player()
screen.onkey(turtle_player.move,"Up")
car_manager = CarManager()

scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.cars:
        # if car.distance(turtle_player) < 30:
        #     print(car.distance(turtle_player))
        if car.distance(turtle_player) < 20:
            game_is_on=False
            scoreboard.game_over()
    # detect successfully crossing
    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()
