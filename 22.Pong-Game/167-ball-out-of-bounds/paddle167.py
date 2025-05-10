# Move paddle logic here.
from turtle import Turtle


class Paddle(Turtle): #inherit from the Turtle class

    def __init__(self, position):   #pass in position parameter (4:10)
        '''To get all the attributes from Turtle class, use the super() keyword'''
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        #Move the paddle to the far right
        self.penup()
        self.goto(position) #self.goto(350, 0)
                


    '''Convert go_up() and go_down() functions for this class (5:10)'''
    # '''Sec 22 V 162 (3:05) create custom function to move paddle up'''
    # def go_up():
    # new_y = paddle.ycor() + 20 #move up 20 pixels
    # paddle.goto(paddle.xcor(), new_y) #stay at the same x-cor. Move up 20 pixels

    # def go_down():
    # new_y = paddle.ycor() - 20 
    # paddle.goto(paddle.xcor(), new_y) 

    def go_up(self):
        new_y = self.ycor() + 20 #move up 20 pixels
        self.goto(self.xcor(), new_y) #stay at the same x-cor. Move up 20 pixels

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(), new_y) 