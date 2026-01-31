#Top Level Dictionary
from tkinter import *
import requests
win=Tk()
win.geometry("500x300")
win.title("Dictionary App")

entry = Entry(win,font=("Arial",15))
entry.pack(pady=10)

def Search():
    word = entry.get()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    res = requests.get(url)
    data = res.json()
    meaning.config(text=data[0]["meanings"][0]["definitions"][0]["definition"])

searchButton = Button(win,text="Search",command=Search)
searchButton.pack()

meaning = Label(win,text="Meaning will Appear Here:")
meaning.pack(pady=10)

win.mainloop()