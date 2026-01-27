#Tkinter Frame
from tkinter import*
window = Tk()
window.title("Intro Tkinter")
window.geometry("700x400")

def f1():
    print("Welcome to Tkinter")

frame1 = Frame(master=window,bg="black",height=200,width=100)
frame1.pack(side=TOP)
frame2 = Frame(master=window,bg="green",height=400,width=200)
frame2.pack(side=LEFT)
frame3 = Frame(master=window,bg="red",height=100,width=300)
frame3.pack(side=RIGHT)

window.mainloop()