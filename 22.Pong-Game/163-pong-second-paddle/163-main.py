#163 focuses on creating the opponent's paddle (2nd paddle)

# Set up the Main Screen
from turtle import Screen, Turtle
from paddle import Paddle #import paddle.py

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong")

# Turn off the animation so the pong paddle doesn't show up in the middle at first
screen.tracer(0)


'''Move paddle code to its own classs'''
# # Create the pong paddle. (Use Turtle class)
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# #Move the paddle to the far right
# paddle.penup()
# paddle.goto(350, 0)

# '''Sec 22 V 162 (3:05) create custom function to move paddle up'''
# def go_up():
#   new_y = paddle.ycor() + 20 #move up 20 pixels
#   paddle.goto(paddle.xcor(), new_y) #stay at the same x-cor. Move up 20 pixels

# def go_down():
#   new_y = paddle.ycor() - 20 
#   paddle.goto(paddle.xcor(), new_y) 


# Set up the two paddles that accept a Tuple as the position
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# separate class makes it easy to add a 3rd paddle, like top_paddle((270,0))

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
  screen.update()



#Make the screen persist
screen.exitonclick()