from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        '''Call update_scoreboard() when class initialized in 168-main.py'''
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear() # prevent new score overriding the previous score
        # Place the Left Paddle score up to the left
        self.goto(-100, 200)
        # Write the score to the screen
        self.write(self.l_score, align="center", font=("Courier", 88, "normal"))

        # Place the Right Paddle score up to the left
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 88, "normal"))

    
    '''Method to track left paddle score'''
    def l_point(self):
        self.l_score += 1
        '''Call update_scoreboard() to force a refresh of the score after awarding 1 pt to lefty'''
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1   # add r_score created in __init__() function
        self.update_scoreboard() # force refresh of score