#Top Level Calculator
from tkinter import *
from PIL import Image, ImageTk
win = Tk()
win.geometry("600x600")
win.title("Top Level")

label = Label(win, text="Let's Calculate")
label.pack()
label2 = Label(win, text="Press the below button to open Calculator")
label2.pack()

upload = Image.open("Codingal/Class 43/Calculator.png")
upload = upload.resize((400,400))
image = ImageTk.PhotoImage(upload)

label = Label(win,image=image,bg="blue")
label.place(x=180,y=90)

def Createcal():
    tp = Toplevel(win)
    tp.geometry("350x350")
    tp.title("Calculator")

    def Calculator(Operation):
        n1 = float(e1.get())
        n2 = float(e2.get())
        if Operation == '+':
            r = n1 + n2
        elif Operation == '-':
            r = n1 - n2
        elif Operation == '*':
            r = n1 * n2
        else:
            r = n1 / n2
        out.delete(0, END)
        out.insert(0, r)

    def add():
        Calculator('+')
    def sub():
        Calculator('-')
    def mul():
        Calculator('*')
    def div():
        Calculator('/')

    Label(tp, text="Enter Number 1").place(x=20, y=20)
    e1 = Entry(tp)
    e1.place(x=130, y=20)

    Label(tp, text="Enter Number 2").place(x=20, y=60)
    e2 = Entry(tp)
    e2.place(x=130, y=60)

    Button(tp, text="+", width=5, command=add).place(x=20, y=100)
    Button(tp, text="-", width=5, command=sub).place(x=80, y=100)
    Button(tp, text="*", width=5, command=mul).place(x=140, y=100)
    Button(tp, text="/", width=5, command=div).place(x=200, y=100)

    Label(tp, text="Solution").place(x=20, y=150)
    out = Entry(tp)
    out.place(x=100, y=150)

button = Button(win, text="Calculator", command=Createcal)
button.pack()

win.mainloop()