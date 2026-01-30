#Calculator
import tkinter as tk

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

    out.delete(0, tk.END)
    out.insert(0, r)

def add():
    Calculator('+')
def sub():
    Calculator('-')
def mul():
    Calculator('*')
def div():
    Calculator('/')


window = tk.Tk()
window.title("Calculator")
window.geometry("250x300")

tk.Label(window, text="Number 1").place(x=20, y=20)
e1 = tk.Entry(window)
e1.place(x=100, y=20)

tk.Label(window, text="Number 2").place(x=20, y=60)
e2 = tk.Entry(window)
e2.place(x=100, y=60)

tk.Button(window, text="+", width=5, command=add).place(x=20, y=100)
tk.Button(window, text="-", width=5, command=sub).place(x=80, y=100)
tk.Button(window, text="*", width=5, command=mul).place(x=140, y=100)
tk.Button(window, text="/", width=5, command=div).place(x=200, y=100)

tk.Label(window, text="Output").place(x=20, y=150)
out = tk.Entry(window)
out.place(x=100, y=150)

window.mainloop()