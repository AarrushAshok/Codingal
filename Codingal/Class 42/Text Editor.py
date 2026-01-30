#Text Editor
from tkinter import *
win =Tk()
win.title("Notepad")
win.geometry("600x600")

def saveText():
    content = textArea.get()
    with open("note.txt","w") as f:
        f.write(content)

btn = Button(win,text="save",command=saveText)
btn.pack()

textArea = Text(win)
textArea.pack(fill="both",expand=True)

win.mainloop()