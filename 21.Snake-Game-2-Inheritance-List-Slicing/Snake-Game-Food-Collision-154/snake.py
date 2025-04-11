from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Sec 20 V.150 at (7:15) Constants to restrict snake free movement
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        #segments = []
        self.segments = []
        self.create_snake()
        #Sec 20. V150 - create attribute for head of snake
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            '''Updated in Sec 21 V 157'''
            self.add_segment(position)
            # new_segment = Turtle("square")
            # new_segment.color("white")
            # new_segment.penup()
            # new_segment.goto(position)
            # #segments.append(new_segment)
            # self.segments.append(new_segment)
    
    '''Added add_segment and extend in Sec 21 V 157'''
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        #segments.append(new_segment)
        self.segments.append(new_segment)


    def extend(self):
        #Add a new segment to the snake
                        #get hold of last position with -1 ie [1, 2, 3]
        self.add_segment(self.segments[-1].position())


    def move(self):
        ''' range comes from C Language (not pure python) Can't use keywords start, stop, step '''
        # for seg_num in range(start= 2, stop= 0, step= -1):
        # for seg_num in range(start= len(segments) - 1, stop= 0, step= -1):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        #outside for loop, grap the first segment and move it forward 20 paces
        # self.segments[0].forward(20)
        # self.segments[0].forward(MOVE_DISTANCE)
        '''Changed in Sec 20 V150 (5:15) to head for segments[0]'''
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        # self.segments[0].setheading(90)
        # self.head.setheading(90)
        if self.head.heading() != DOWN: #can't go up if already heading down
            self.head.setheading(UP)

    def down(self):
        # pass
        # self.head.setheading(270)
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self):
        # pass
        # self.head.setheading(180)
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self):
        # pass
        # self.head.setheading(0) 
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT) 

