
#jaspar pirs 04.02.25
import tkinter as tk
from PIL import Image, ImageTk


def main():
    # DPI teadlikkuse seadistamine kõrge DPI ekraanide jaoks
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception as e:
        print(e)

    aken = tk.Tk()
    aken.title("Jaspari ulesanded")
    aken.geometry("400x400")
    aken.resizable(False, True)

    pilt = Image.open("pikanid.jpg")
    pilt = pilt.resize((200, 200))
    foto = ImageTk.PhotoImage(pilt)
    pilt = pilt.crop ((0, 0, 100, 100))
    
    

    label = tk.Label(aken, text="LiL till aka Jan", font=("Arial", 16, "bold"), fg="blue").pack()
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial, 12"))
    tekst.pack()
    
    def loe_fail(tktext):
        with open(tk.text, 'r', encoding='utf-8') as file:
            return file.read()

    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
    aken.mainloop()

if __name__ == "__main__":
    main()

