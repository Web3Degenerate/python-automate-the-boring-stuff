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
        self.move_speed = 0.1 # so we can speed up the ball over the course of the game. See 6:30 in V168.


    def move(self):
        #increase x and y axis
        '''Replaced +10 with self.x_move and self.y_move'''
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Vertical (y-axis) Bounce - Change direction vertically
    def bounce_y(self):
        #make it minus
        self.y_move *= -1
        self.move_speed *= 0.9 # increase ball speed when it hits the left paddle.


    # Horizontal (x-axis) Bounce - Change direction horizontally
    def bounce_x(self):
        #make it minus
        self.x_move *= -1
        self.move_speed *= 0.9 # increase ball speed when it hits the right paddle.

    def reset_position(self):
        # Go to the original position at (0, 0)
        self.goto(0, 0)
        '''Reset the ball speed when we reset_position the ball'''
        self.move_speed = 0.1
        '''Additionally, drop ball in center and go the OPPOSITE DIRECTION with bounce_x() method above'''
        self.bounce_x()