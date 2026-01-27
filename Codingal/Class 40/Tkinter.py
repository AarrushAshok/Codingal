#Tkinter
from tkinter import*
window = Tk()
window.title("Intro Tkinter")
window.geometry("300x200")

#Frame:
frame = Frame(master=window,bg="lightblue",height=390,width=690)
frame.pack()

window.mainloop()