#Tkinter Button
from tkinter import*
window = Tk()
window.title("Intro Tkinter")
window.geometry("700x400")

def f1():
    print("Welcome to Tkinter")

button1 = Button(master=window,bg="green",text="submit",fg="black",command=f1,borderwidth=10,relief="ridge")
button2 = Button(master=window,bg="green",text="submit",fg="black",command=f1,borderwidth=10,relief="sunken")
button3 = Button(master=window,bg="green",text="submit",fg="black",command=f1,borderwidth=10,relief="groove")
button4 = Button(master=window,bg="green",text="submit",fg="black",command=f1,borderwidth=10,relief="raised")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

window.mainloop()