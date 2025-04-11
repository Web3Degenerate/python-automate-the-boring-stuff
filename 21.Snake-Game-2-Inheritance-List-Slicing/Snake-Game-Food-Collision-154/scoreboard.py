#Created in Sec 21. V. 155.
from turtle import Turtle

ALIGNMENT = "center"
'''Font has to be a Tuple, not just a string'''
# FONT = ("Arial", 24, "normal")
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle): #inherits from Turtle

    def __init__(self):
        super().__init__()
        #score starts at 0
        self.score = 0
        self.color("white") # Set color and CSS and such before write to screen below

        #move scoreboard from center to top of screen
        '''color and go to must be before self.write()'''
        self.penup()
        self.goto(0, 270)

        # Use Turtle write method to display text on screen
        # self.write(f"Score: {self.score}", align="center", font="Arial:24, normal")
        '''Font has to be a Tuple, not just a string'''

        # MOVE into update_scoreboard()
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()

        #Sec 21. V155. at (4:20) - hide turtle when screen loads
        self.hideturtle()



    '''At 8:20 in Sec 21 V155, Combine multiple self.write stmts into own function, update_scoreboard()'''
    def update_scoreboard(self):
        '''Font has to be a Tuple, not just a string'''
        # (9:25) Sec 21.V155 - move text to CONSTANTS on top
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.score += 1

        #Clear the previous score. Otherwise it just writes the new number(s) on top of the old
        self.clear()

        # MOVE into update_scoreboard()
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()

    '''Add Wall Collision in Sec 21 V 156 at 240'''
    def game_over(self):
        # Have message go to center of screen
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

