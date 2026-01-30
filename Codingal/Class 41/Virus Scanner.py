#Virus Scanner
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")

def virus():
    messagebox.showwarning("Alert!Virus Detected")

button = Button(window,text="Virus Scan in Progress",command=virus)
button.place(x=40,y=80)

root.mainloop()