from turtle import Screen, Turtle
import time

#Sec 20 - V 149 - import Snake class
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")



snake = Snake()

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




screen.exitonclick()