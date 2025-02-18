#Install package colorgram.py: https://pypi.org/project/colorgram.py/
''' Run `pip install colorgram.py` '''

import colorgram
import turtle as turtle_module #alias 'turtle_module
import random

# Docs: TO extract colors from an image: 
# colors = colorgram.extract('name.jpg', 30)
# second param is number of colors to extract

colors = colorgram.extract('image.jpg', 30)
# print(colors) #returns list of RGB colors. 

rgb_colors = []
for color in colors: 
    rgb_colors.append(color.rgb) #specify rgb or hsl etc. 

# print(rgb_colors) #returns in format we don't need

# returns [Rgb(r=245, g=243, b=238), Rgb(r=247, g=242, b=244), etc]
# we want [(245, 243, 238), (247, 242, 244), etc]

'''Solution to get format we need, change how we tap into data in for loop'''
formatted_rgb_colors = []
for c in colors: 
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    '''CREATE OUR TUPLE WITH DESIRED (R, G, B) VALUES'''
    new_color = (r, g, b)
    formatted_rgb_colors.append(new_color)

# print(formatted_rgb_colors)

# for c in colors, then didn't use c (same 3 values repeated)
#[(168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102), (168, 99, 102)]

# She said to delete first two (245, 243, 238) (246, 242, 244) "background?" Closer to 250 250 250
# [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


# Now we can use color_list to create a 10 x 10 diagram of color dots with turtle
'''Per this stack overflow article, we had to use colormode(255)'''
'''https://stackoverflow.com/questions/16778324/what-does-bad-color-sequence-mean-in-python-turtle'''
turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest") #speed up drawing process
tim.penup() #we don't need to see the line showing turtle path. still draws dots
tim.hideturtle() #removes the cursor, which was the triangle in this example. 
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

#use turtle dot() method
# two params 1 - size, 2- color
# tim.dot(20, (202, 164, 110))

# To set starting point at bottom left of screen use .setheading(225)
tim.setheading(225)
tim.forward(300) #don't start until gets to bottom left. 
tim.setheading(0) #turn in desired direction


#number_of_dots will keep track of when we need to reset our typewriter
number_of_dots = 100

# for _ in range(10):
for dot_count in range(1, number_of_dots + 1): #range(1, 101) to get the last dot (100th dot)
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    '''Reset typewriter at end of each 'row', which is blocks of 10!! '''
    if dot_count % 10 == 0: #means count is 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
        '''We need this block to repeat after every row (typewriter reset)'''
        # Reset position outside of for loop which is just going across screen (left => right) 10 dots
        tim.setheading(90) #face up
        tim.forward(50) #move forward by 50 paces
        tim.setheading(180) #turn left at end of line
        tim.forward(500) # move 10 x 50 paces so 500 (go back to left like typewriter)
        tim.setheading(0) #turn right


#========= To persist Turlte output, create Screen object ==========
screen = turtle_module.Screen()
screen.exitonclick()