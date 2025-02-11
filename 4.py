import tkinter as tk
def kuva_varv():
    print("Nupp on vajutatud")
def main():
    aken = tk.Tk()
    aken.geometry("400x100")
   
    nupp1 = tk.Button(aken,  bg="red", fg="white", font=("Arial", 16), command=kuva_varv)
    nupp2 = tk.Button(aken, bg="orange", fg="white", font=("Arial", 16), command=kuva_varv)
    nupp3 = tk.Button(aken,  bg="yellow", fg="black", font=("Arial", 16), command=kuva_varv)
    nupp4 = tk.Button(aken,  bg="green", fg="white", font=("Arial", 16), command=kuva_varv)
    nupp5 = tk.Button(aken,  bg="blue", fg="white", font=("Arial", 16), command=kuva_varv)
    vastus = tk.Label(aken, text=f"Siia tuleb vastus")
    vastus.pack(side="bottom", expand="true", fill="x", anchor="center")
    
    nupp1.pack(side="left", expand="true", fill="x")
    nupp2.pack(side="left", expand="true", fill="x")
    nupp3.pack(side="left", expand="true", fill="x")
    nupp4.pack(side="left", expand="true", fill="x")
    nupp5.pack(side="left", expand="true", fill="x")

    
    aken.mainloop()

if __name__ == "__main__":
    main()