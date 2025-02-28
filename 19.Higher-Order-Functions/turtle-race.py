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

is_race_on = False
all_turtles = [] #Resume (2:36) Sec 19 V144

starting_line_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=starting_line_position[turtle_index])
    all_turtles.append(new_turtle)

    # n=-1
    # new_turtle.goto(x=-230, y=starting_line_position.pop(n+1))
    # print(f"value of n is now {n}")
    print(f"This is numerical value of {turtle_index}.")

# won't start until user input (which color) is received
if user_bet: 
    is_race_on = True


while is_race_on: 
    # Add for loop to handle each of our six turtles
    for turtle in all_turtles:
        #Get the winning turtle by catching the first one to reach x-coordinate of 230 (250 max - 20 turtle size)
        if turtle.xcor() > 230:
            is_race_on = False #end the race
            # print(turtle.color()) #mltiple ('yellow', 'yellow') returns pencolor and fillcolor
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle wins. Collect your winnings!")
            else:
                print(f"You Lost! {winning_color} turtle wins. The house wins again!")
        rand_distance = random.randint(0, 10) #randit is inclusive
        turtle.forward(rand_distance)


# ============================
screen.exitonclick()
# screen.exitonclick()