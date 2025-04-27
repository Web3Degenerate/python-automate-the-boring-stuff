
'''
Objectives
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep Score
'''


# Set up the Main Screen
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong")

# Turn off the animation so the pong paddle doesn't show up in the middle at first
screen.tracer(0)


# Create the pong paddle. (Use Turtle class)
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
#Move the paddle to the far right
paddle.penup()
paddle.goto(350, 0)


'''Sec 22 V 162 (3:05) create custom function to move paddle up'''
def go_up():
  new_y = paddle.ycor() + 20 #move up 20 pixels
  paddle.goto(paddle.xcor(), new_y) #stay at the same x-cor. Move up 20 pixels

def go_down():
  new_y = paddle.ycor() - 20 
  paddle.goto(paddle.xcor(), new_y) 

# Set up our event listeners
screen.listen()
screen.onkey(go_up, "Up") #the Up Arrow key serves as the trigger
screen.onkey(go_down, "Down")





'''Create a while loop to update the screen with our animation off (screen.tracer(0))'''
game_is_on = True
while game_is_on:
  screen.update()







#Make the screen persist
screen.exitonclick()