# tkinter comes with python
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




#===================================================
# ==== **kw - kwargs Optional Arguemnts ================
# ==============================================

# Resume Sec 27 - V.206 - Setting Default Values for Optional Arguments

# Unlimited Arguments Example: 

def add(*args):
    print(args)

add(3, 5, 6) # jjust prints 3, 5, 6 on SAME line


def add_for_loop(*args):
    for n in args:
        print(n)


add_for_loop(3, 5, 6) # prints 3, 5, 6 on new line each



def add_actual(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


add_actual(3, 5, 6) # returns 14...if you `return sum` ;)


# Keep the GUI window open ===== MUST BE AT END OF PROGRAM ====================
window.mainloop() #keeps window on screen, listens for input
