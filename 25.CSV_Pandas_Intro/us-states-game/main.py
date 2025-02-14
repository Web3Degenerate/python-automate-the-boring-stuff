import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# Get user input: 
answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")
print(answer_state)


'''Solution if we didn't already have the x, y coordinates in our csv. Just an FYI'''
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) #event listener, calls our custom function

# turtle.mainloop() #alternative way to keep our screen open, despite code not finish running

# #==== Previous way we Persisted Turtle output, but it closes on click & we need to click so comment out
# # instead use the `turtle.mainloop()` function above
# # screen.exitonclick()
'''====================================================================================='''