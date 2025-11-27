from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        '''Sec 24. V.182 (1:00) Add attribute self.high_score'''
        '''Sec 24. V184 (2:05) Remove self.high_score and read from data.txt'''
        # self.high_score = 0
        '''use with keyword so we don't have to worry about closing the file. Python will manage it for us.'''
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    '''Sec 24. V182 (1:21) Replace game_over method with reset()'''
    def reset(self):
        #check user score against high_score. If so, update high_score 
        if self.score > self.high_score:
            self.high_score = self.score
            '''Sec 24. V184 (3:45) Update high score in data.txt'''
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0 #reset score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #
    #

    def increase_score(self):
        self.score += 1
        # self.clear() # move to update_scoreboard
        self.update_scoreboard()
