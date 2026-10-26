
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Button Demo")

def hello():
    label.config(text="You've clicked me!")

button = Button(window, text="Click me", command=hello)
button.pack()

label = Label(
    window,
    text="Hello World!",
    font=("Times New Roman", 12),
    fg="white",
    bg="black"
)
label.pack()

window.mainloop()
