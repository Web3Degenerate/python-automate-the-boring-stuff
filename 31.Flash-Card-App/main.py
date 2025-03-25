from tkinter import *
import pandas # (Sec 31, vid 238 at 1:30))
import random

BACKGROUND_COLOR = "#B1DDC6"

'''READ from our updated CSV list of remaining words to learn (Sec 31 V242 (4:30))'''
to_learn = {}
try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  # data = pandas.read_csv("data/french_words.csv") #dataframe
  original_data = pandas.read_csv("data/french_words.csv") 
  to_learn = original_data.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records")

# to_learn = data.to_dict(orient="records") # records list like [{column -> value},...,{column->value}]
# print(to_learn)

## Sec 31, Vid 240 - (2:15) - set current_card empty dictionary to pass from next_card() to flip_card()
current_card = {}

#add next_card function in Sec 31, vid 238 at 00:45)
def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer) #pass in the id of our flip_timer (7:40 Sec 31, Vid 240)
  # pass
  current_card = random.choice(to_learn)
  # print(current_card["French"])
  canvas.itemconfig(card_title, text="French", fill="black")
  canvas.itemconfig(card_word, text=current_card["French"], fill="black")
  # Sec 31, Vid 240 - (5:20) Set the French side back to white background and black text
  canvas.itemconfig(card_background, image=card_front_img)
  # Sec 31, Vid 240 - (6:05) - Add 3 second flip for EACH card
  # window.after(3000, func=flip_card)
  # Sec 31, Vid 240 - 7:45 - set up NEW flip_timer to wait for 3 seconds
  flip_timer = window.after(3000, func=flip_card)

def flip_card(): ## Sec 31, Vid 240 - (1:15) - function to flip card after 3 seconds
  canvas.itemconfig(card_title, text="English", fill="white")
  canvas.itemconfig(card_word, text=current_card["English"], fill="white")
  # Sec 31, Vid 240 (4:00)
  canvas.itemconfig(card_background, image=card_back_img)


#Add is_known new function is_known in Sec 31 Video 242 (00:55)
def is_known():
  to_learn.remove(current_card) #remove current card from to_learn dictionary
  print(len(to_learn))
  '''Use Pandas to create a NEW dataframe to store remaining words to learn (Sec 31 V242 (3:10))'''
  data = pandas.DataFrame(to_learn)
  # data.to_csv("data/words_to_learn.csv") #overwrites the csv file every time to_learn dictionary is udpated
  '''Sec 31, Vid 242 (8:05) set index to False to avoid increasing index columns on each save'''
  data.to_csv("data/words_to_learn.csv", index=False)
  
  next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# my_image = PhotoImage(file="images/card_front.png")
# button = Button(image=my_image, highlightthickness=0)

# Sec 31, Vid 240 - (00:40) - Set 3 second timer for card to flip
# window.after(3000, func=flip_card)
# Sec 31, Vid 240 - (7:10) - change to global and add to global variables in next_card() function
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")

# Sec 31, Vid 240 - (3:05) - set to card_background variable 
# You have to create card_back_img down here, not in a funciton above for it to work (3:40)
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

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

#Change known_button function to new function is_known in Sec 31 Video 242 (00:50)
# known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
#place right button on grid
known_button.grid(row=1, column=1)


# (Sec 31, vid 238 at 7:00)) - Call the next_card() function to load a word in our french dictionary
next_card()


window.mainloop()