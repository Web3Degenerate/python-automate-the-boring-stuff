from turtle import Turtle
import random

'''we want the Food class to inherit from the Turtle Class (Sec 21. Vid 154 (~1:45))'''
# class Food:
#     def __init__(self):
#         pass
        # instead of creating our turtle object as an attribute of this class
        # like this: self.food = Turtle()

class Food(Turtle):

    def __init__(self):
        super().__init__() #gives you access to all the Turtle methods
        #example shape()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #creates 10 x 10 circle. Default is 20 x 20.
        self.color("blue")
        self.speed("fastest")
        #set random x and y coordinates with the random module
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y) #go to a random x,y coordinate