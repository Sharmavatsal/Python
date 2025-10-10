# show alert box when button is clicked

import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo('msg','from hehe...')
root = tk.Tk()

canvas = tk.Canvas(root, width="200", height="300")
canvas.pack()

button1 = tk.Button(root, text="Click me", command=on_click)
button1.pack(pady=10)
root.mainloop()


#

import tkinter as tk
def add_foo():
    result=int(tbox1.get())+int(tbox2.get())
    label1.config(text="JAWAB : "+str(result))
root=tk.Tk()
tbox1=tk.Entry()

tbox1=tk.Entry(root)
tbox1.pack(pady=20)

tbox2=tk.Entry(root)
tbox2.pack(pady=25)

button1=tk.Button(root,text='ADD',command=add_foo)
button1.pack()

label1=tk.Label(root,text="Answer here")
label1.pack()
root.mainloop()