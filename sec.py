import random
from tkinter import *


def degistir():
    dosya = open("sinif","r")
    dizi = dosya.readlines()


    
    yazi.config(text=random.choice(dizi))
    #print (dizi)

pencere=Tk()
pencere.geometry("300x100")
baslik = pencere.title("Öğrenci Seçim Programı")
yazi=Label(pencere)
yazi.config(text="Öğrenci isimleri Buraya gelecek\n")
yazi.pack()

dugme=Button(pencere)
dugme.config(text="Öğrenci Seç")
dugme.config(command=degistir)
dugme.pack()
pencere.mainloop()
input()
