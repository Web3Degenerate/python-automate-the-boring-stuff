# Sec 19. V143

from turtle import Turtle, Screen
import turtle as turtle_module
import random


# Turtle.colormode(255)
turtle_module.colormode(255)

# screen = turtle_module.Screen()
screen = Screen()



#setup turtle method captures to set exact width of playing screen
screen.setup(width=500, height=400)

#user input
user_bet = screen.textinput(title="Illegal Ninja Turtle Race Bets!", prompt="Which color turtle bet on. Enter color: ")
print(user_bet)



#move turtles to starting line - use turtle goto() method
# x, y coordinates. Center screen 0, 0. 
# Max Y values 200/-200
# Max x values 250/-250

colors = ["red", "#FFA500", "yellow", "green", "blue", "purple"]



# tim = Turtle(shape="turtle")
# tim.colormode(255)

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()


starting_line_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=starting_line_position[turtle_index])

    # n=-1
    # tim.goto(x=-230, y=starting_line_position.pop(n+1))
    # print(f"value of n is now {n}")

    print(f"This is numerical value of {turtle_index}.")


# ============================
screen.exitonclick()
# screen.exitonclick()