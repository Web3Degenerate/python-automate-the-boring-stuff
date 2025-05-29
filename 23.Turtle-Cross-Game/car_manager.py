from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# class CarManager:
#     pass

class CarManager:
    
    def __init__(self):
        self.all_cars = []
        # Didn't use super().__init__() here
        '''Sec 23. V178 (3:40) increase car speed every level'''
        self.car_speed = STARTING_MOVE_DISTANCE #(initally set to constant of 10)

    def create_car(self):
        '''To slow down massive block of cars (every 0.1 seconds create new one), only run this function ROUGHLY 1 in 6 times, like roll of dice'''
        random_chance = random.randint(1,6)
        if random_chance == 1:
            # Create random car somewhere along the y-axis
            new_car = Turtle("square")
                                # multipy length by 2, width by 1 (keep the same)
            new_car.shapesize(stretch_wid=1, stretch_len=2) # set the size of the car with .shapesize()
            new_car.penup() # don't draw
            new_car.color(random.choice(COLORS)) #randomly pull color from global variable above
            '''using random_y = random.choice(-250, 250) gave me error 2 positional arguments but 3 given'''
            random_y = random.randint(-250, 250) # where goes - random y-axis position b/t -250 to 250
            new_car.goto(300, random_y)

            # Append to our list of all_cars[]
            '''Requires self keyword to add to list in this case'''
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            '''Sec 23. V178 (3:50) Set car speed to variable set up in init'''
            # car.backward(STARTING_MOVE_DISTANCE) # move backwards 5 pixels/paces
            car.backward(self.car_speed)


    '''Created Level up in Sec 23. V178 (3:30)'''
    def level_up(self):
        self.car_speed += MOVE_INCREMENT #increment speed by 5 each level





