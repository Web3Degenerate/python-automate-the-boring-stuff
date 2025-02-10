from turtle import Turtle, Screen
# import heroes
import random

tim = Turtle()
# Set shape of turtle: https://docs.python.org/3/library/turtle.html#turtle.shape
tim.shape("turtle")
tim.color("red")

#move and turn - Draw Square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

#Draw Square with fewer lines of code
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#Dashed Line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup() #stop drawing
#     tim.forward(10)
#     tim.pendown() #start drawing


# Draw Shapes (various angles)
# 5 sides - 360/5 = 72 degrees

#Function dynamically handles the num_sides
def custom_draw_shape(num_sides):
    # Equation: 
    # num_sides = 5
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

#Ranom Colors
colors = ["red", "blue", "black", "green"]

'''Make the custom_draw_shape start at 3 and go up to 10'''
# With for range() function, set the outter limit (2nd param) at desired plus 1
## for range(3, 11) would be 3 to 10
### you can use _ or something like for shape_side_n in range(3, 11): 
for _ in range(3, 11):
    tim.color(random.choice(colors))
    custom_draw_shape(_)


#=============== Draw to screen command ===================================
# create screen object from Turtle module
screen = Screen()
screen.exitonclick()


#pip install heroes example: 
# print(heroes.gen())