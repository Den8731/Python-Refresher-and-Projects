from tkinter import *

window = Tk()

window.geometry("300x300")
label = Label(window, text="Hello World!")
label.pack()
#Everything comes before this function. Anything after it will not run, or the program won't run properly
window.mainloop()