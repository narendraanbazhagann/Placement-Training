import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "Hello, Tkinter!")

app = tk.Tk()
app.title("Simple Tkinter App")

button = tk.Button(app, text="Click Me", command=show_message)
button.pack(pady=20)

app.mainloop()
