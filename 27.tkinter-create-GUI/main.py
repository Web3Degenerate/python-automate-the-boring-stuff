# tkinter comes with python
# to import all classes use `import tkinter *`
import tkinter

window = tkinter.Tk()

window.title("Our First GUI")
window.minsize(width=500, height=300)




my_label = tkinter.Label(text="This is the label", font=("Arial", 24, "bold"))
#print to screen with .pack()
# https://docs.python.org/3/library/tkinter.html#the-packer
my_label.pack() #default "top" center
# my_label.pack(side="left")
# my_label.pack(side="right")
my_label.pack(side="bottom", expand=True) #expand take up all space it can


#using tkinter, we can set text with either way: 
my_label['text'] = "New Text"
my_label.config(text="Newer Text")


#===================================================
# ==== Buttons with custom click functions ================
# Pass to window in the Button() function, param `command=<funciton>`
# ==============================================

def button_clicked(): 
    print("I got clicked") #prints text to the command line
    user_input = input.get()
    # my_label.config(text="I got clicked")
    my_label.config(text=user_input)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()




#===================================================
# ==== **kw - kwargs Optional Arguemnts ================
# Reviewed in S.27. V.209. 
# ==============================================


#===================================================
# ==== Entry Class ================
# Input Fields - used KWARGS with .get() in S.27.V.209
# ==============================================


input = tkinter.Entry(width=10)
input.pack()
input.get() #so I can optionally tap into kwargs I want without throwing error on skipped ones







# Keep the GUI window open ===== MUST BE AT END OF PROGRAM ====================
window.mainloop() #keeps window on screen, listens for input
