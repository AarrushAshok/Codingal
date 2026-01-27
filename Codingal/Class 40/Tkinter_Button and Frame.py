#Tkinter Button and Frame
from tkinter import*
window = Tk()
window.title("Intro Tkinter")
window.geometry("700x400")

entry = Entry(master=window)
entry.pack()

def f1():
    text = entry.get()
    helloText.config(text="Hi"+ text)

helloText = Label(master=window,text="hello",bg="blue",fg="green")
helloText.pack()

frame1 = Frame(master=window,bg="black",height=200,width=100)
frame1.pack(side=TOP)

frame2 = Frame(master=window,bg="green",height=400,width=200)
frame2.pack(side=LEFT)

frame3 = Frame(master=window,bg="red",height=100,width=300)
frame3.pack(side=RIGHT)

button1 = Button(master=window,bg="green",text="submit",fg="black",command=f1,borderwidth=10,relief="ridge")

window.mainloop()