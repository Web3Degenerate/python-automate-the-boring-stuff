import import_module_example

print(import_module_example.example_variable)

# Then import a class `Turtle` from external Turtle module to create Turtle Object
import turtle


#Alternatively, use from - import just the Turtle class
from turtle import Turtle

# Use parenthesis to actually construct the turtle object
timmy = turtle.Turtle()

print(timmy) #prints object <turtle.Turtle object at 0x0000026AD0848F10>

