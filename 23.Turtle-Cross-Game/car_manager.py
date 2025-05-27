from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# class CarManager:
#     pass

class CarManager:
    
    def __init__(self):
        all_card = []
        # Didn't use super().__init__() here

    def create_cars(self):
        # Create random car somewhere along the y-axis
        new_car = Turtle("square")
                            # multipy width by 2, length by 1 (keep the same)
        new_car.shapesize(stretch_wid=2, stretch_len=1) # set the size of the car with .shapesize()
        new_car.penup() # don't draw
        new_car.color(random.choice(COLORS)) #randomly pull color from global variable above
        random_y = random.choice(-250, 250) # where goes - random y-axis position b/t -250 to 250
        new_car.goto(300, random_y)

        # Append to our list of all_cars[]
        '''Requires self keyword to add to list in this case'''
        self.all_cars.append(new_car)
        







