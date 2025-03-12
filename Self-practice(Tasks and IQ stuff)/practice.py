import tkinter as tk
from tkinter import *



app = tk.Tk()
app.title("Simple App hue hue")
app.geometry("400x400")

# def something():
#     name = name_entry
#     if name:
        

name_label = tk.Label(app,text = "Enter a name")
name_label.pack(padx = 10, pady = 10)

name_entry = tk.Entry(app, text = "Jai ho")
# name_entry.pack(padx = 10, pady = 10)

button = tk.Button(app, text = "Bhai Dabao", overrelief="raised")
button.pack(padx = 10, pady = 10)

app.mainloop()