# Sec 21 V 158 - Add Slicing

  #import food class

# from turtle import Screen, Turtle #importing Turtle in food.py and snake.py
from turtle import Screen
import time

#Sec 20 - V 149 - import Snake class
from snake import Snake
#Sec 21 - V154 - import Food class
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0) #not sure when added


snake = Snake()
food = Food()
'''Sec 21. V.155 (4:30) Add Scoreboard'''
scoreboard = Scoreboard()


# Sec 20. V150 - Add screen.listen() to control snake with keyboard (arrow keys)
'''Create the up, down, left and right functions in our Snake.py Class '''
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# while game is running
game_is_on = True
while game_is_on:
    screen.update()
    '''Using time module, add a 1 second delay (Sec 20. V.148 (6:40))'''
    time.sleep(0.1) #one-tenth second delay after all three segments have moved (faster)
    
    snake.move() # Don't forget to call the move function from our Snake class!

    ''' Detect Snake - Food Collision in Sec 23. V. 154 (7:48)'''
    # use turtle.distance(x, y=None)
    # check distance from snake head to food (10x10 pixels) is less than 15 pixels = collision
    if snake.head.distance(food) < 15:
        # print("collision")
        '''Pull in new refresh() method from food.py (Sec 21 V.154 at 9:55)'''
        food.refresh()

        # at 7:30 in Sec 21, V.155 import Scoreboard
        scoreboard.increase_score()

        '''Added Snake extend in Sec 21 V 157'''
        snake.extend()


    '''Add Detect Wall Collision in Sec 21 V 156'''
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #exit the while loop
        game_is_on = False
        scoreboard.game_over()

    '''Sec 21 V 157 (3:35) Detect collision with Tail'''
    # If the head collides with any segment in the tail - Trigger game_over

    '''This would always catch the had since the had size is 10 pixels'''
    # for segment in snake.segments:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()


    '''Sec 21 V 158 at (1:34) use Slicing like piano_keys[2:5] '''
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

 
# screen was instantly closing at end of game because misspelled 'align" in scoreboard game_over()
# screen.update()
# time.sleep(3)

screen.exitonclick()

