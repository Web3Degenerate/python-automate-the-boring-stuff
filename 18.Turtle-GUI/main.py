from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# Set shape of turtle: https://docs.python.org/3/library/turtle.html#turtle.shape
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

#move and turn - Draw Square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

#Draw Square with fewer lines of code
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# create screen object from Turtle module
screen = Screen()
screen.exitonclick()
