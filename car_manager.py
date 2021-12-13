from turtle import Turtle, Screen
import random
screen = Screen()
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_START = 280
X_FINISH = -280

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.new_x = 0
        self.y = 0
        self.spawn_frequency = 8
        self.hideturtle()

    def spawn(self):
        ran_no = random.randint(1,10)
        if ran_no > self.spawn_frequency:
            # spawn point
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            self.y = random.randint(-11, 11) * 20
            new_car.goto(X_START, self.y)
            self.all_cars.append(new_car)
        # move to other side of screen

    def move(self):
        for car in self.all_cars:
            self.new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(self.new_x, car.ycor())

    def next_level(self):
        self.new_x += MOVE_INCREMENT
        self.spawn_frequency -= 1








