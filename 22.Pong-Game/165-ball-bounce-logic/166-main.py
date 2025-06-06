'''This adds the paddle collision logic in Sec 22. V.166'''

#163 focuses on creating the opponent's paddle (2nd paddle)

# Set up the Main Screen
from turtle import Screen, Turtle
from paddle import Paddle #import paddle.py
from ball import Ball #import ball.py
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong")

# Turn off the animation so the pong paddle doesn't show up in the middle at first
screen.tracer(0)


# Set up the two paddles that accept a Tuple as the position
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# separate class makes it easy to add a 3rd paddle, like top_paddle((270,0))

# Add the ball from ball.py
ball = Ball()


# Set up our event listeners
screen.listen()
''' importing go_up and go_down so call with r_paddle.go_up or <object>.go_up'''
# screen.onkey(go_up, "Up") 
# screen.onkey(go_down, "Down")
'''Right paddle with use Up/Down arrow. Left paddle will use 'w' up and 's' down '''
screen.onkey(r_paddle.go_up, "Up") 
screen.onkey(r_paddle.go_down, "Down")
#left paddle
screen.onkey(l_paddle.go_up, "w") 
screen.onkey(l_paddle.go_down, "s")




'''Create a while loop to update the screen with our animation off (screen.tracer(0))'''
game_is_on = True
while game_is_on:
    '''import time module to sleep between refreshes'''
    time.sleep(0.1) # 0.1 second sleep
    screen.update()
    '''Call ball.move() to move ball from center'''
    ball.move()

    '''Sec 22, V.165 (5:23) - Detect collision with wall'''
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    '''Sec 22, V.166 (2:31) - Detect collision with r_paddle'''
    ''' Right and Left Paddle/Ball Detection Logic Broken down: '''
    # ball.distance(r_paddle) < 50: Within 50 pixels of right paddle
    # ball.xcor() > 340: Ball has gone far enough RIGHT to be past the RIGHT paddle

    # ball.distance(l_paddle) < 50: Within 50 pixels of LEFT paddle
    # ball.xcor() < -340:  Ball has gone far enough left to be past the LEFT paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made Contact with paddle")
        '''Forgot to add `ball.bounce_x()` and ball went right through r_paddle (5/8/2025)'''
        ball.bounce_x() 


#Make the screen persist
screen.exitonclick()