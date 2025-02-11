import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def open_file():
    documents_path = Path.home() / "Documents"
    filename = filedialog.askopenfilename(
        initialdir=documents_path,
        filetypes=(
            ("Tekstifailid", "*.txt"),
            ("Pythoni failid", ("*.py", "*.pyx")),
            ("Kõik failid", "*.*")
        ),
        title="Vali failikene"
    )
    if filename:
        file_label.config(text=f"Valitud fail: {filename}")
    else:
        file_label.config(text="Faili ei valitud.")

def save_directory():
    pass

aken = tk.Tk()
aken.title("Peamine aken")
aken.geometry("450x400")

label = tk.Label(aken, text="Pildi suurus 200x200", font="Arial 24")
label.pack(pady=10)

inputtxt = tk.Text(aken, height=10, width=50)
inputtxt.pack(pady=10)

salvesta_pildid = tk.Button(aken, text="Salvesta pildid", command=save_directory)
salvesta_pildid.pack(pady=10, side="bottom")

open_button = tk.Button(aken, text="Vali failid", command=open_file)
open_button.pack(pady=10, side="bottom")

file_label = tk.Label(aken, text="")
file_label.pack(pady=10)


aken.mainloop()