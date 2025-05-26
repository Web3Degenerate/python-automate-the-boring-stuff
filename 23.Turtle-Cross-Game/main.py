import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) #turn off tracer


'''Instantiate Player class from player.py'''
player = Player()


'''Get Player to move up with arrow (Sec 23. V175, 2:55)'''
screen.listen()
screen.onkey("Up")
# .go_up() is a custom function we created in player.py
screen.onkey(player.go_up, "Up") #dont use .go_up(), triggers immediately


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
