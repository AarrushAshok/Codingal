#Event Handler
from tkinter import *
win = Tk()
win.geometry("500x500")

def handle_keypress(event):
    print(event.char)

win.bind("<Key>",handle_keypress)

def handle_click(event):
    print("Mouse first button was clicked")
def handle_click2(event):
    print("Mouse second button was clicked")
def handle_click3(event):
    print("Mouse third button was clicked")

win.bind("<Button-1>",handle_click)
win.bind("<Button-2>",handle_click2)
win.bind("<Button-3>",handle_click3)

win.mainloop()