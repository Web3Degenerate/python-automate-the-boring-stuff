from turtle import Turtle

class Ball(Turtle): #import from Turtle

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        '''Added in 165'''
        self.x_move = 10
        self.y_move = 10


    def move(self):
        #increase x and y axis
        '''Replaced +10 with self.x_move and self.y_move'''
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        #make it minus
        self.y_move *= -1
        