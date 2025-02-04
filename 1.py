import tkinter as tk
#jaspar pirs 04.02.25


# Peafunktsioon, mis loob Tkinteri akna ja lisab sinna sildi ja nupu
def main():
    aken = tk.Tk()
    aken.title("Jaspari ulesanded")
    aken.geometry("400x300")
    aken.resizable(True, False)
    label = tk.Label(aken, text="Tere, maailm!").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

# Käivitame peafunktsiooni
if __name__ == "__main__":
    main()