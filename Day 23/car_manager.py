# Import necessary modules
from turtle import Turtle
import random

#Define a list of colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

#Set the initial distance a car moves in each step and the increment when leveling up
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#Define a class
class CarManager:

    def __init__(self):
        #Initialize an empty list to store all the car objects
        self.all_cars = []
        #Set the initial speed of the cars
        self.car_speed = STARTING_MOVE_DISTANCE

    #Create new car
    def create_car(self):
        random_chance = random.randint(1, 6) #random number from 1 to 6
        # If the random number is 1, create a new car
        if random_chance == 1:
            new_car = Turtle("square") #Make car shape of a square
            
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()

            # Set a random color
            new_car.color(random.choice(COLORS))
            #Set a random y-coordinate for car
            random_y = random.randint(-250, 250)

            #Position the car on the right side of the screen
            new_car.goto(300, random_y)

            #Add the new car to the list of all cars
            self.all_cars.append(new_car)

    #Way to make the cars to the left
    def move_cars(self):
        for car in self.all_cars:
            # Move the car backward based on its current speed
            car.backward(self.car_speed)

    #Increase the speed of the cars for higher levels
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
