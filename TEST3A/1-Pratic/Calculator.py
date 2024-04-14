
num1 = int(input("Sayi giriniz num1:"))
num2 = int(input("sayi giriniz num2:"))
action = str(input("İslem Seciniz : Topla (a) , Çıkart(s) , Çarp(m) , Böl (d)  -> "))
 # Topla= add /çıkart = sub / Çarp = multi / 
# işlemler ingilizce karşılıkları olarak yazılmıştır carpma ve cikartma kısaltmaları birbirine çakışmaktadır.

print("Sonuç :" , end="")
if action == "a":
    print(num1+num2)
elif action =="s":
    print(num1-num2)
elif action == "m":
    print(num1*num2)
else:
    print(num1/num2)            

