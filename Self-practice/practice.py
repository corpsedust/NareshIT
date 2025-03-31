import tkinter as tk
from tkinter import messagebox



app = tk.Tk()
app.title("Simple App hue hue")
app.geometry("400x400")

def something():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Bakchodi",message = f"Lol Gay {name}")
    else:
        messagebox.showinfo("Tumse na ho paayega", message= "Rehene de Bhai")
        

name_label = tk.Label(app,text = "Enter a name")
name_label.pack(padx = 10, pady = 10)

name_entry = tk.Entry(app, text = "Jai ho")
name_entry.pack(padx = 10, pady = 10)

button = tk.Button(app, text = "Bhai Dabao", overrelief="raised", command = something)
button.pack(padx = 10, pady = 10)

app.mainloop()