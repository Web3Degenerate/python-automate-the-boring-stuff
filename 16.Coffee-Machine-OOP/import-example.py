import import_module_example

print(import_module_example.example_variable)

# Then import a class `Turtle` from external Turtle module to create Turtle Object
import turtle


#Alternatively, use from - import just the Turtle class
# import turtle
from turtle import Turtle

# Use parenthesis to actually construct the turtle object
# using from turtle import Turtle (instead of just `import turtle` 
# changes how we can call the Turtle() obejct):
# timmy = turtle.Turtle()
timmy = Turtle()

print(timmy) #prints object <turtle.Turtle object at 0x0000026AD0848F10> (location saved at in computer's memory)

