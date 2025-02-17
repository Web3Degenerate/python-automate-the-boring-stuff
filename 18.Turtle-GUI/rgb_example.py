import turtle as t
import random 

tim = t.Turtle()
t.colormode(255) 


#Ranom Colors
# colors = ["red", "blue", "black", "green"]
def random_color(): 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    '''GENERATE our Tuple with the random values for RGB'''
    # random_color = (r, g, b)
    # return random_color
    return (r, g, b)


#Random Directions 0 - east, 90 - north, 180 - west, 270 - south
directions = [0, 90, 180, 270]

tim.pensize(15) #turtle built in pensize() method
tim.speed("fastest")

# Move 200 times
for _ in range(200): 
    # tim.color(random.choice(colors)) #random colors
    tim.color(random_color())
    tim.forward(30)
    #turtle built in function setheading()
    tim.setheading(random.choice(directions))


"""RESUME AT SEC 18, V.134 Python Tuples and Generate random RGB colors"""


#=============== Draw to screen command ===================================
# create screen object from Turtle module
# screen = Screen()
# screen.exitonclick()


#pip install heroes example: 
# print(heroes.gen())