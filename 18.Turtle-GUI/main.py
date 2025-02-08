from turtle import Turtle, Screen
import heroes

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
for _ in range(15):
    tim.forward(10)
    tim.penup() #stop drawing
    tim.forward(10)
    tim.pendown() #start drawing



#=============== Draw to screen command ===================================
# create screen object from Turtle module
screen = Screen()
screen.exitonclick()


#pip install heroes example: 
print(heroes.gen())