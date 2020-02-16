import random
from tkinter import *


ogr=[]
secim=0
basım=10
modu=1

def ekle():
    dosya = open("sinif.txt",mode="r",encoding="utf-8")

    if ogr==[]:
        for i in dosya.readlines():
            ogr.append(i)
    else:       
        yazi.config(text="Kayıtlı Öğrenci Zaten Eklemişsiniz!\n")
def mod():
    global modu,basım

    modu = modu+1
    modu=modu%10
    if modu==0:
        modu=1
    print(modu)
    dugme2.config(text=modu)
       
    
    
def degistir():
    global basım,modu,secim
    if ogr ==[]:
        yazi.config(text="Kayıtlı öğrenci kalmadı!\nÖğrenci Ekleden sonra Öğrenci Seç butonuna tekrar basınız.")

    else:   
        rast=random.choice(ogr)
        
        yazi.config(text=rast)
        basım=basım+1
        secim=basım%modu
        print (basım)
        print (modu)
        print (secim)
        
        if secim==0:
            print ("Öğrenci silinmedi")
            basim=4
            
        else:
            print ("Öğrenci silindi")
            ogr.remove(rast)
        

    
pencere=Tk()

pencere.geometry("400x200")
baslik = pencere.title("Öğrenci Seçim Programı")

yazi=Label(pencere,text="Öğrenci isimleri buraya gelecek\nÖğrenci Ekle butonuna ardından Öğrenci Seç butonuna basınız.")
yazi.pack()

dugme=Button(pencere,text="Öğrenci Seç",command=degistir)
dugme.pack()

dugme1=Button(pencere,text="Öğrenci Ekle",command=ekle)
dugme1.pack()

dugme2=Button(pencere,text="Seçim Ayarı",command=mod)
dugme2.pack()


pencere.mainloop()

