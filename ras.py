import random

from tkinter import *


from tkinter import messagebox

pencere = Tk()

pencere.title("Recep Çakır")
pencere.geometry("300x100")

uygulama = Frame(pencere)
uygulama.grid()
def degistir():
    yazi.config(text="İşte yazı değişti. Söyle, mutlu musun?")

def dialog():
    liste = [3, 4, 5, 6, "Elma", 3.14, 5.324]
    dosya = open("sinif","r")
   
    dizi = dosya.readlines()
    var = messagebox.showinfo("Sen Seçildin", random.choice(dizi))
    #print (dizi)
    #print(dizi.rstrip('s'))
    
button1 = Button(uygulama, text=" Öğrenci Seç ", width=30, command=dialog)
button1.grid(padx=10, pady=10)



# formu çiz
pencere.mainloop()


