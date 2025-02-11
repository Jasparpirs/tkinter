#jaspar 
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    def kuva_sisestus():
        laenusumma = int(sisestus1.get())  # Võtab esimese sisestuse
        kuuintressimäär = float(sisestus2.get())/12/100  # Võtab teise sisestuse
        maksete_arv = int(sisestus3.get())*12  # Võtab kolmanda sisestuse
        igakuine_makse = laenusumma * kuuintressimäär / (1 - (1 + kuuintressimäär) ** -maksete_arv)
        print(f"Igakuine makse: {igakuine_makse:.2f}")
       
        
    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5, fill="x")
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5)
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5)
   
    label1 = tk.Label(frame,  text="Laenusumma (€):").pack(side="left")
    sisestus1 = tk.Entry(frame)
    sisestus1.pack(side="left", fill="x", expand=True)
    
   
    label2  = tk.Label(frame2, text="Aastane intressimäär (%):").pack(side="left")
    sisestus2 = tk.Entry(frame2)
    sisestus2.pack(side="left", fill="x")
    
    label3 = tk.Label(frame3, text="Laenuperiood (aastates): ").pack(side="left")
    sisestus3 = tk.Entry(frame3)
    sisestus3.pack(side="left",fill="x")
   
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    
    aken.mainloop()

if __name__ == "__main__":
    main()