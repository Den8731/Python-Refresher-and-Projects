from _pyrepl.commands import delete, backspace
from tkinter import *

window = Tk()
window.geometry("500x500")
entryOut = Label(window, text="Hello, World!")

#Button functions set
def submit_entry():
    message = "Hello,"
    userInput = entry.get()
    entryOut.config(text="Hello, " + userInput)
    entryOut.pack()

def delete_entry():
    userInput = entry.delete(0, END)

def backspace_button():
    userInput = entry.delete(len(entry.get()) - 1)

entry = Entry(window)
entry.pack()


submitButton = Button(window,text="Submit",command = submit_entry)
submitButton.pack()

delete_button = Button(window,text="Delete",command = delete_entry)
delete_button.pack()

backspace_button = Button(window,text="Backspace",command = backspace_button)
backspace_button.pack()


window.mainloop()