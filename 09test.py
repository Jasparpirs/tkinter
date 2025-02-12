import tkinter as tk
from tkinter import messagebox



# Loome peamise akna
aken = tk.Tk()
aken.title("Peaaken")
aken.geometry("200x400")

frame = tk.Frame(aken)
frame.pack(pady=5, padx=5, fill="x")
frame2 = tk.Frame(aken)
frame2.pack(pady=5, padx=5)
frame3 = tk.Frame(aken)
frame3.pack(pady=5, padx=5)
   

label1 = tk.Label(frame,  text="Kasutaja id:").pack(side="left")
sisestus1 = tk.Entry()
sisestus1.pack(side="top", fill="x", expand=True)
    

def show_selection():
    print("Valitud värv:", selected_color.get())

# StringVar, mis hoiab valitud värvi nime
selected_color = tk.StringVar(value="red")


radio_red = tk.Radiobutton(aken, text="väike", variable=selected_color, value="red")
radio_green = tk.Radiobutton(aken, text="Suur", variable=selected_color, value="green")
radio_blue = tk.Radiobutton(aken, text="Pere", variable=selected_color, value="blue")
radio_red.pack()
radio_green.pack()
radio_blue.pack()



var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

def show_selection():
    print(var1.get(), var2.get(), var3.get())

# Loome märkeruudud
checkbox1 = tk.Checkbutton(aken, text="Juust(+1Eur)", variable=var1)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni(+1.5Eur)", variable=var2)
checkbox3 = tk.Checkbutton(aken, text="Seen(+1Eur)", variable=var3)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()



# Valikute määramine ja valitud väärtuse hoidja
valikud = ["Kuller(+3Eur)", "Tulen ise järgi(+0Eur)"]
selected_option = tk.StringVar()
selected_option.set("Vali üksus")

# Dropdown menüü loomine
dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()

def valik():
    print("Valitud üksus:", selected_option.get())



aken.mainloop()


def open_new_window():
   aken = tk.Tk()
aken.title("Messageboxi näide")

def show_message():
    messagebox.showinfo("Teadete aken", "Tere maailm!")

btn_message = tk.Button(aken, text="Näita teadet", command=show_message)
btn_message.pack()

aken.mainloop()