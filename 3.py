import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "reio is monkey")

root = tk.Tk()
root.title("Message Window")

label = tk.Label(root, text="reio is monkey")
label.pack(pady=20)

button = tk.Button(root, text="Show Message", command=show_message)
button.pack(pady=10)

root.mainloop()