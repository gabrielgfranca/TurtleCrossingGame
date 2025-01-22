from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_new_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            cars = Turtle()
            cars.shape("square")
            cars.shapesize(stretch_wid=1, stretch_len=2)
            cars.color(random.choice(COLORS))
            cars.penup()
            random_y = random.randint(-250, 250)
            cars.goto(300, random_y)
            self.all_cars.append(cars)


    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

