from tkinter import *
import pandas # (Sec 31, vid 238 at 1:30))
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv") #dataframe
to_learn = data.to_dict(orient="records") # records list like [{column -> value},...,{column->value}]
print(to_learn)

#add next_card function in Sec 31, vid 238 at 00:45)
def next_card():
  # pass
  current_card = random.choice(to_learn)
  # print(current_card["French"])
  canvas.itemconfig(card_title, text="French")
  canvas.itemconfig(card_word, text=current_card["French"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# my_image = PhotoImage(file="images/card_front.png")
# button = Button(image=my_image, highlightthickness=0)



canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
#Add some text to our card
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) #get rid of outter white box
canvas.grid(row=0, column=0, columnspan=2) #columnspan=2 to get our buttons below to layout properly


# Create two buttons (Sec 31, vid 236 at 8:25)
## WRONG BUTTON
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card) #add next_card function in Sec 31, vid 238 at 00:45)
#place wrong image on grd
unknown_button.grid(row=1, column=0)

## CORRECT Button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
#place right button on grid
known_button.grid(row=1, column=1)


# (Sec 31, vid 238 at 7:00)) - Call the next_card() function to load a word in our french dictionary
next_card()


window.mainloop()