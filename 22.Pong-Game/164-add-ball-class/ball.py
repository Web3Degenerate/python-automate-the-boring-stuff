from turtle import Turtle

class Ball(Turtle): #import from Turtle

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()


    def move(self):
        #increase x and y axis
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)