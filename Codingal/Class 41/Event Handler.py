#Event Handler
from tkinter import *
win = Tk()
win.geometry("500x500")

def handle_keypress(event):
    print(event.char)

win.bind("<Key>",handle_keypress)

win.mainloop()