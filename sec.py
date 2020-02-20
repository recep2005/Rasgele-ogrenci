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
        yazi.config(text="Öğrenciler Eklendi!\n")
    else:       
        yazi.config(text="Hala Listede Kayıtlı Öğrenci Var!\n")
def mod():
    global modu,basım

    modu = modu+1
    modu=modu%10
    if modu==0:
        modu=1
    print(modu)
    dugme2.config(text="Seçim Ayar="+str(modu))
    if modu==1:
        yazi.config(text="Hiç Bir Öğrenci\nListeden Düşmez!")
    else:
        yazi.config(text="Her "+str(modu)+" Seçimde\n Bir Öğrenci\nListeden Düşmez!")
        
    
    
def degistir():
    global basım,modu,secim
    if ogr ==[]:
        yazi.config(text="Kayıtlı Öğrenci Kalmadı!\n Öğrenci Ekle Butonuna Basın!.")

    else:   
        rast=random.choice(ogr)
        
        yazi.config(text="Seçilen Öğrenci\n"+rast)
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

pencere.geometry("360x110")
baslik = pencere.title("Öğrenci Seçim Programı")

yazi=Label(pencere,relief=SOLID, text="Öğrenci isimleri\n buraya gelecek\nÖğrenci Ekle butonuna ardından \nÖğrenci Seç butonuna basınız.")
yazi.place(x=130, y=10, width = 220, heigh=90)


dugme=Button(pencere,relief=SOLID,text="Öğrenci Seç",command=degistir, width = 10 )
dugme.place(x=10, y=10)


dugme1=Button(pencere,relief=SOLID,text="Öğrenci Ekle",command=ekle,width = 10)
dugme1.place(x=10, y=40)


dugme2=Button(pencere,relief=SOLID,text="Seçim Ayar=1",command=mod, width = 10)

dugme2.place(x=10, y=70)
yazi2=Label(pencere,font=("",6,""), text="Recep Çakır")
yazi2.place(x=280, y=100, width = 80, heigh=10)

pencere.mainloop()

