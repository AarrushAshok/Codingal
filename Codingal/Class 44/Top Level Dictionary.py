#Top Level Dictionary
from tkinter import *
import requests
win=Tk()
win.geometry("400x500")
win.title("Dictionary App")

entry = Entry(win,font=("Arial",15))
entry.pack(pady=10)

def Search():
    word = entry.get()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    res = requests.get(url)
    data = res.json()
    print(data)

searchButton = Button(win,text="Search",command=Search)
searchButton.pack()

meaning = Label(win,text="Meaning will Appear Here:")
meaning.pack(pady=10)

win.mainloop()