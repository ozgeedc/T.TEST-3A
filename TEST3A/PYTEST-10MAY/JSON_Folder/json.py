import json

n={"id":30, "name":"Özge", "city":"İstanbul"} # Bir sözlük (dictionary) oluşturuyoruz. Bu sözlük, veri içeriğini temsil eder

with open('info.json', 'r+',encoding="UTF-8")as dosya: #info.json dosyasını açar 
    veri = json.load(dosya)  #info.json(dosya)klasörünü '' veri'' değişkenine atıyoruz


aranan_id = 26
yeni_name ="Serpil Nur" #Güncellenmek istenen veri

for ticket in veri.get("info",[]):
    if ticket.get("id") == aranan_id:   # aranan veri ile ID eşitse
     print("ID Bulundu")
    ticket["name"] = yeni_name  #"name" alanını güncelle 
    with open('info.json','w', encoding="UTF-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=2)
        print(f"Datadaki {aranan_id} id'sine sahip verin (name)değişkeni {yeni_name} olarak güncellendi")

    break
else:
    print("İstenilen ID'ye sahip veri bulanamadı")                 