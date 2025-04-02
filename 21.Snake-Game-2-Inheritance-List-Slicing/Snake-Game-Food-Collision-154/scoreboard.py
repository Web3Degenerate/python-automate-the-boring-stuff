#Created in Sec 21. V. 155.
from turtle import Turtle

class Scoreboard(Turtle): #inherits from Turtle

    def __init__(self):
        super().__init__()
        #score starts at 0
        self.score = 0
        # Use Turtle write method to display text on screen
        # self.write(f"Score: {self.score}", align="center", font="Arial:24, normal")
        '''Font has to be a Tuple, not just a string'''
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

        #resume Sec 21. V155. at (4:20)