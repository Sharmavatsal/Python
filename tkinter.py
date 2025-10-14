# show alert box when button is clicked with tkinter

import tkinter as tk 
from tkinter import messagebox

def on_click():
    messagebox.showinfo('msg','from Darkheaven...')
root = tk.Tk()

canvas = tk.Canvas(root, width="200", height="300")
canvas.pack() # grid and place are also used

button1 = tk.Button(root, text="Click me", command=on_click)
button1.pack(pady=10)
root.mainloop()


# program to add two numbers with tkinter


import tkinter as tk
from tkinter import messagebox

def add_foo():
    result = int(tbox1.get()) + int(tbox2.get())
    label1.config(text="JAWAB : " + str(result))
    messagebox.showinfo("Answer", "JAWAB : " + str(result))  # Show result in messagebox

root = tk.Tk()
root.geometry("400x450")  # size of window
root.minsize(100,150)     # min size of window
root.maxsize(700,750)     # max size of window  

label1 = tk.Label(root, text="Enter first number :")
label1.pack()

tbox1 = tk.Entry(root)
tbox1.pack(pady=20)

label2 = tk.Label(root, text="Enter second number :")
label2.pack()

tbox2 = tk.Entry(root)
tbox2.pack(pady=25)

button1 = tk.Button(root, text='ADD', command=add_foo)
button1.pack()

label1 = tk.Label(root, text="Answer here")
label1.pack()

root.mainloop()


# practice (label)

import tkinter as tk

root=tk.Tk()
root.geometry("400x450") # size of window
label=tk.Label(root,text="This is a Label")
label.pack(padx=500,pady=100)
root.mainloop()


# practice (to change label text through button)


import tkinter as tk

root=tk.Tk()
def on_click():
    label.config(text="Button Clicked")
root.geometry("400x450") # size of window
button=tk.Button(root,text="Click",command=on_click)
button.pack()
label=tk.Label(root,text="Button  is Clicked")
label.pack(padx=500,pady=100)
root.mainloop()

# code with proper design 

import tkinter as tk

def add_foo():
    try:
        result = int(tbox1.get()) + int(tbox2.get())
        label1.config(text="JAWAB : " + str(result))
    except ValueError:
        label1.config(text="Invalid input!")

# Root window setup
root = tk.Tk()
root.title("Dark Add Machine")
root.geometry("300x300")
root.configure(bg="#121212")  # Dark background

# Styling options
entry_style = {
    "bg": "#1e1e1e",
    "fg": "white",
    "insertbackground": "red",
    "highlightbackground": "red",
    "highlightcolor": "red",
    "relief": "flat",
    "font": ("Segoe UI", 12)
}

button_style = {
    "bg": "red",
    "fg": "white",
    "activebackground": "#ff4c4c",
    "activeforeground": "black",
    "font": ("Segoe UI", 12, "bold"),
    "bd": 0,
    "padx": 10,
    "pady": 5
}

label_style = {
    "bg": "#121212",
    "fg": "red",
    "font": ("Segoe UI", 12, "bold")
}

# Widgets
tbox1 = tk.Entry(root, **entry_style)
tbox1.pack(pady=(30, 10))

tbox2 = tk.Entry(root, **entry_style)
tbox2.pack(pady=(10, 20))

button1 = tk.Button(root, text="ADD", command=add_foo, **button_style)
button1.pack()

label1 = tk.Label(root, text="Answer here", **label_style)
label1.pack(pady=20)

# Start GUI
root.mainloop()







# code with more design 

import tkinter as tk

def calculate():
    try:
        num1 = float(tbox1.get())
        num2 = float(tbox2.get())
        op = operation.get()

        if op == "Add":
            result = num1 + num2
        elif op == "Subtract":
            result = num1 - num2
        elif op == "Multiply":
            result = num1 * num2
        elif op == "Divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        label_result.config(text=f"JAWAB : {result:.2f}", fg="#00ffcc")
    except ZeroDivisionError:
        label_result.config(text="Cannot divide by zero!", fg="#ff4444")
    except ValueError:
        label_result.config(text="Invalid input!", fg="#ff4444")

def clear_all():
    tbox1.delete(0, tk.END)
    tbox2.delete(0, tk.END)
    label_result.config(text="Answer here", fg="red")
    tbox1.focus()

def on_enter(e):
    e.widget.config(bg="#ff4c4c")

def on_leave(e):
    e.widget.config(bg="red")

# Root window
root = tk.Tk()
root.title("Dark Themed Calculator")
root.geometry("350x400")
root.configure(bg="#121212")

# Fonts and Colors
entry_font = ("Segoe UI", 12)
label_font = ("Segoe UI", 13, "bold")
button_font = ("Segoe UI", 12, "bold")
option_font = ("Segoe UI", 11)

# Entry Style
entry_style = {
    "bg": "#1e1e1e", "fg": "white", "insertbackground": "red",
    "highlightbackground": "red", "highlightcolor": "red",
    "relief": "flat", "font": entry_font, "width": 20
}

# Entry Fields
tbox1 = tk.Entry(root, **entry_style)
tbox1.pack(pady=(30, 10))

tbox2 = tk.Entry(root, **entry_style)
tbox2.pack(pady=(10, 10))

# Dropdown for operation
operation = tk.StringVar(value="Add")
options = ["Add", "Subtract", "Multiply", "Divide"]
dropdown = tk.OptionMenu(root, operation, *options)
dropdown.config(bg="#1e1e1e", fg="white", font=option_font,
                activebackground="red", activeforeground="white",
                highlightthickness=0, bd=0)
dropdown["menu"].config(bg="#1e1e1e", fg="white", activebackground="red")
dropdown.pack(pady=(5, 15))

# Buttons
btn_calc = tk.Button(root, text="CALCULATE", command=calculate,
                     bg="red", fg="white", font=button_font,
                     activebackground="#ff4c4c", activeforeground="black",
                     bd=0, padx=15, pady=7, cursor="hand2")
btn_calc.pack(pady=(10, 5))
btn_calc.bind("<Enter>", on_enter)
btn_calc.bind("<Leave>", on_leave)

btn_clear = tk.Button(root, text="CLEAR", command=clear_all,
                      bg="red", fg="white", font=button_font,
                      activebackground="#ff4c4c", activeforeground="black",
                      bd=0, padx=15, pady=7, cursor="hand2")
btn_clear.pack(pady=5)
btn_clear.bind("<Enter>", on_enter)
btn_clear.bind("<Leave>", on_leave)

# Result Label
label_result = tk.Label(root, text="Answer here", font=label_font,
                        bg="#121212", fg="red")
label_result.pack(pady=(30, 10))

# Focus first entry on start
tbox1.focus()

# Run the application
root.mainloop()

