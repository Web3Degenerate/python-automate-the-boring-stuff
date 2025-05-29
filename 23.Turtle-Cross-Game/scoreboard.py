from turtle import Turtle

FONT = ("Courier", 24, "normal")


# class Scoreboard:
#     pass

class Scoreboard(Turtle): #make Scoreboard class a subset of the Turtle class. (Inherit from Turtle Class)
    
    '''Sec 23. V179. (1:09) - super init when want class to do everything parent class can do'''
    def __init__(self):
        super().__init__()
        self.level = 1 #default to level 1
        self.hideturtle() #hide turtle by default
        self.penup()
        self.goto(-280, 250) #top left corner
        # self.write(f"Level: {self.level}", align="left", font=FONT) # move to update_scoreboard function below
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() #remove old level so it doesn't write new level on top of old level(s)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0) #place turtle in center
        self.color("red")
        self.write("Game Over", align="center", font=FONT)