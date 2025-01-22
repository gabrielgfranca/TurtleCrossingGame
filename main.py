import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
CAR_SPEED_INCREMENT = 10


# Screen Config
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Turtle Config
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.going_forward)

# Car Config
car_manager = CarManager()

# Scoreboard Config
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if the player has hit the top of the edge
    if player.ycor() >= FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        car_manager.car_speed += CAR_SPEED_INCREMENT
        scoreboard.level_up()



screen.exitonclick()
