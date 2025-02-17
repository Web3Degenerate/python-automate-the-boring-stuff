import turtle as t
import random 

"""SEC 18, V.135 Spirograph"""

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


tim.speed("fastest")

def draw_spirograph(size_of_gap):    
    '''(1) division always returns float, even if 10/2 = 5.0'''
    '''(2) range() only take int, so wrap division in int()'''
    for _ in range(int(360 / size_of_gap)):    
        tim.color(random_color())
        tim.circle(100) #param is the radius size
            # print(tim.heading()) # returns 0.0
            # current_heading = tim.heading()
            # tim.setheading(current_heading + 10) #param takes angle
        # REFACTOR to one line: 
        # tim.setheading(tim.heading() + 10)
        tim.setheading(tim.heading() + size_of_gap)


#call custom function with size_of_gap = 5
draw_spirograph(5)

#=============== Draw to screen command ===================================
# using "import turtle as t", so call "t.Screen()"
screen = t.Screen()
screen.exitonclick()


#pip install heroes example: 
# print(heroes.gen())