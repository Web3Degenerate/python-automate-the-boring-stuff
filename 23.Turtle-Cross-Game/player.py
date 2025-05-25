from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# class Player:
    # pass

class Player(Turtle): # player inherits from Turtle Class so player can do everything that Turtle class can do.

    def __init__(self):
        super().__init__() # Needs super.init
        self.shape("turtle")
        self.penup() # so doesn't draw while moving
        self.goto(STARTING_POSITION) # globakl Tuple variable above
        self.setheading(90) # face north