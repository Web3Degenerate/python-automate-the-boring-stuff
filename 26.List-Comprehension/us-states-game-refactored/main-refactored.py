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
        #refactor four lines of code into 1: 
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        #create new csv file
        # new_data.to_csv("states_to_learn.csv")
        
        #or just print to console
        print(new_data)
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
        state_data = data[data.state == answer_state]

        t.goto(state_data.x.item(), state_data.y.item()) #move turtle to x, y coordinates of state

        '''pandas.Series.item - call .item() to get single value, here state name like so:'''
        t.write(state_data.state.item())


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