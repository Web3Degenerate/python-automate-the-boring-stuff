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

        self.go_to_start() #replace duplicate code below in Sec 23. V178
        # self.goto(STARTING_POSITION) # global Tuple variable above

        self.setheading(90) # face north


    def go_up(self):
        self.forward(MOVE_DISTANCE)


    '''Sec 23, V 178'''
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else: 
            return False