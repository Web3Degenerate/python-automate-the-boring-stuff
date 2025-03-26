from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")


''' Replace with for in loop below - Sec 20, V.147 '''
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

# with for loop with tuples
'''Tuples Covered in Day 18 '''
#=======Replaced With for in loop below from Sec 20. V 148 ===================================================
# starting_positions = [(0,0), (-20, 0), (-40, 0)]

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)
#==========================================================

# === Sec 20. V 148 =====

starting_positions = [(0,0), (-20, 0), (-40, 0)]

segments = []


for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    # print(new_segment)
    segments.append(new_segment)



# screen.update()

# while game is running
game_is_on = True
while game_is_on:
    '''Using time module, add a 1 second delay (Sec 20. V.148 (6:40))'''
    time.sleep(0.1) #one-tenth second delay after all three segments have moved (faster)
    
    # for seg in segments:
    #     seg.forward(20)
    #     screen.update()
        # time.sleep(1) #one second delay after each segment (quite slow)

    ''' range comes from C Language (not pure python) Can't use keywords start, stop, step '''
    # for seg_num in range(start= 2, stop= 0, step= -1):
    # for seg_num in range(start= len(segments) - 1, stop= 0, step= -1):
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    #outside for loop, grap the first segment and move it forward 20 paces
    segments[0].forward(20)
    # segments[0].left(90) #continuous circle


# Grab just the first of three segements
    #segments[0].left(90)

# PICK UP at Sec 20, V. 149

screen.exitonclick()