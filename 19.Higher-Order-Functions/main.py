# Sec 19. V140

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_right():
    tim.setheading(0)
    tim.forward(10)

def move_left():
    tim.setheading(180)
    tim.forward(10)

#Her solution
def _move_lefter(): 
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # or tim.left(10)


def move_up():
    tim.setheading(90)
    tim.forward(10)

def move_down():
    tim.setheading(270)
    tim.forward(10)


# === Her Solution (more precision, left / right adjust angle by 10) 
# Then just provide forward and backward capability ============

#Her solution
def move_righter(): 
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    # or tim.right(10)

#Her solution
def move_lefter(): 
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # or tim.left(10)

def move_forwards():
    tim.forward(10)

def move_backwards(): 
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()


# ========================================
screen.listen()
# screen.onkey(key="space", funct=move_right)
'''MUST use fun not your own custom `funct` '''
screen.onkey(key="l", fun=move_right)
screen.onkey(key="j", fun=move_left)
screen.onkey(key="i", fun=move_up)
screen.onkey(key="k", fun=move_down)

# Her Methods
screen.onkey(key="d", fun=move_righter)
screen.onkey(key="a", fun=move_lefter)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)

screen.onkey(key="c", fun=clear)

screen.exitonclick()

#===================
# == Turtle Docs ===
# ==================

# onkey: https://docs.python.org/3/library/turtle.html#turtle.onkey
# listen: https://docs.python.org/3/library/turtle.html#turtle.listen

# setheading: https://docs.python.org/3/library/turtle.html#turtle.setheading