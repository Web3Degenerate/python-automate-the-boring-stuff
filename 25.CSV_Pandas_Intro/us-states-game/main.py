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

# data["state"] - pull the state column out as a key
# data.state - pull the state column as an attribute

# pull state column out and turn it into a list
'''data.state.to_list()'''
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    # Get user input: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another State's name?").title()
    # print(answer_state)


    # BREAK out of while loop when user input = 'Exit'
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # Turn missing_states list into a DataFrame
        new_data = pandas.DataFrame(missing_states)
        # Export to CSV in same directory
        new_data.to_csv("states_to_learn.csv")
        break


    # Check If answer_state is one of the states in our 'state' column
    '''USE of if .. in is available ONLY because it has been converted into a LIST'''
    if answer_state in all_states: 
        #Append correct answer to guessed_states list
        guessed_states.append(answer_state)

        #If so (they got it right):
        # create a turtle
        t = turtle.Turtle()
        t.hideturtle() # hide it
        t.penup() #no drawingour states table
        # Pull the x, y coordinates from 
        state_data = data[data.state == answer_state]
        # t.goto(int(state_data.x), int(state_data.y)) 
        # t.goto(int(state_data["x"][0]), int(state_data["y"][0]))
        # t.goto(state_data["x"][0].item(), state_data["y"][0].item())

        t.goto(state_data.x.item(), state_data.y.item()) #move turtle to x, y coordinates of state

        #Create a turtle to write the name of the state @ the state's X, Y coordinates
        # t.write(state_data.state[0]) #raise KeyError(key) from err

        # t.write(state_data.state) #prints out 34 Ohio Name: state, dtype: object
        # t.write(answer_state) #since we already verified user input above, use it to print

        '''pandas.Series.item - call .item() to get single value, here state name like so:'''
        t.write(state_data.state.item())

        #Error: _tkinter.TclError: bad screen distance
        # bad data type. Coordinates are stored as strings, convert int
        # FutureWarning: Calling int on a single element Series is deprecated and will raise
        # a TypeError in the future. 
        # Use int(ser.iloc[0]) instead


screen.exitonclick()


'''Solution if we didn't already have the x, y coordinates in our csv. Just an FYI'''
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) #event listener, calls our custom function

# turtle.mainloop() #alternative way to keep our screen open, despite code not finish running

# #==== Previous way we Persisted Turtle output, but it closes on click & we need to click so comment out
# # instead use the `turtle.mainloop()` function above
# # screen.exitonclick()
'''====================================================================================='''