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


    '''Detect collision with car in Sec 23. V. 177 (1:10)'''
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


    '''Detect successful crossing in Sec 23. V. 178 (0:34)'''
    # Defined as line 280 in player.py constant (FINISH_LINE_Y = 280)
    if player.is_at_finish_line(): 
        player.got_to_start() #reset turtle at starting position for next level
        '''Use new .level_up() function in car_manager.py'''
        car_manager.level_up()




'''Keep Screen up Until We Close it'''
screen.exitonclick()