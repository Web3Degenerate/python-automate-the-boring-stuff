import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#Sec 25. V. 194. Use pandas' read_csv()
# columns state, x, y
data = pandas.read_csv("50_states.csv")


# Get user input: 
answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")
print(answer_state)


# Check If answer_state is one of the states in our 'state' column
    #If so (they got it right):
        #Create a turtle to write the name of the state @ the state's X, Y coordinates
        





'''Solution if we didn't already have the x, y coordinates in our csv. Just an FYI'''
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) #event listener, calls our custom function

# turtle.mainloop() #alternative way to keep our screen open, despite code not finish running

# #==== Previous way we Persisted Turtle output, but it closes on click & we need to click so comment out
# # instead use the `turtle.mainloop()` function above
# # screen.exitonclick()
'''====================================================================================='''