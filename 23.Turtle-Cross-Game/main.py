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

'''Instantiate CarManager class from car_manager.py'''
car_manager = CarManager()

'''Get Player to move up with arrow (Sec 23. V175, 2:55)'''
screen.listen()
screen.onkey("Up")
# .go_up() is a custom function we created in player.py
screen.onkey(player.go_up, "Up") #dont use .go_up(), triggers immediately


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Every refresh of the screen which happens every 0.1 seconds
    car_manager.create_car()
    car_manager.move_cars()
