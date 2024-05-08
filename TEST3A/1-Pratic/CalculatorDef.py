from tkinter import *
import tkinter as tk

def yaz(x):
    print(x)
    a = len(lb1.get())
    lb1.insert(0+a,x)
hesap = 6
s1 = 0
def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float (lb1.get())
    print(hesap)
    print(s1)
    lb1.delete(0,'end')

s2 =0
def hesapla():
    global s2
    s2=float(lb1.get())
    print(s2)
    sonuc = 0
    global hesap
    if hesap == 0: sonuc = s1+s2
    elif hesap == 1: sonuc = s1-s2
    elif hesap == 2:
        sonuc = s1 * s2
    elif hesap == 3:
        sonuc = s1 / s2
    elif hesap == 4:
        sonuc = (s1 * s2)/100
    elif hesap == 5:
        sonuc = s1**s2
    lb1.delete(0,'end')
    lb1.insert(0,sonuc)
def temizle():
    lb1.delete(0,'end')
def geri():
    a = len(lb1.get())
    print(a)
    lb1.delete(a-1,'end')


pencere = tk.Tk()
pencere.geometry('350x450')
pencere.title("  HESAP MAKINESI  ")
lb1 = Entry(font = 'verdana 12 bold',justify =RIGHT)
lb1.place(x=40,y=20)
b=[]
for i in range(1,10):
    b.append(Button(text=i,font='verdana 15 bold',command = lambda x=i:yaz(x)))
sayac = 0
for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=40+j*65,y=100+i*60)
        sayac += 1
islem = []
for i in range(0,4):
    islem.append(Button(font = 'verdana 16 bold',width = 2,command= lambda x=i :islemler(x)))
islem[0]['text']='+'
islem[1]['text']='-'
islem[2]['text']='x'
islem[3]['text']='/'
for i in range(0,4):
    for j in range(0,4):
        islem[i].place(x=90+j*45,y=100+i*60)
ub =Button(text="xʸ",font='verdana 16 bold',width=2,command=lambda x=5:islemler(x))
ub.place(x=105,y=350)
yb = Button(text='%',font='verdana 16 bold',width=2,command=lambda x=4:islemler(x))
yb.place(x=38,y=350)
sb = Button(text='0',font='verdana 16 bold',width=2,command=lambda x=0:yaz(x))
sb.place(x=38,y=280)
nb = Button(text='.',font='verdana 16 bold',width=2,command=lambda x='.':yaz(x))
nb.place(x=104,y=280)
eb = Button(text='=',fg='red',font='verdana 16 bold',width=2,command=hesapla)
eb.place(x=168,y=280)
cb = Button(text='C',font='verdana 16 bold',width=2,command=temizle)
cb.place(x=223,y=350)
gb=Button(text='<-',font='verdana 16 bold',width=2,command=geri)
gb.place(x=166,y=350)
pencere.mainloop()