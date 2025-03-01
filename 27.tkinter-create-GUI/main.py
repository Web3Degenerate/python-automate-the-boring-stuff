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

# Resume S.27. V.209. 



# Keep the GUI window open ===== MUST BE AT END OF PROGRAM ====================
window.mainloop() #keeps window on screen, listens for input
