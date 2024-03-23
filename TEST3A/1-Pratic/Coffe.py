# Kullanıcıya su veya süt ile mi yapılmak istendiğini sormak için:
tercih = input("Kahvenizi su ile mi yoksa süt ile mi yapmak istersiniz? (su/süt): ")

class KahveMakinesi:
    def __init__(self):
        self.su_miktari = 0
        self.kahve_miktari = 0
        self.sut_miktari = 0

    def su_ekle(self, miktar):
        self.su_miktari += miktar
        print(f"{miktar} ml su eklendi.")
        
    def sut_ekle(self, miktar):
        self.sut_miktari += miktar
        print(f"{miktar} ml su eklendi.")    

    def kahve_ekle(self, miktar):
        self.kahve_miktari += miktar
        print(f"{miktar} gr kahve eklendi.")

    def kahve_hazirla(self, sekerli=False, sutlu=False):
        if self.su_miktari >= 200 and self.kahve_miktari >= 10:
            if sekerli:
                print("Şekerli kahveniz hazır! Afiyet olsun.")
            elif sutlu:
                print("Sütlü kahveniz hazır! Afiyet olsun.")
            else:
                print("Kahveniz hazır! Afiyet olsun.")
            self.su_miktari -= 200
            self.sut_miktari -= 200
            self.kahve_miktari -= 10
        else:
            print("Yetersiz su veya kahve miktarı.")

# Kahve makinesi oluştur
kahve_makinesi = KahveMakinesi()

# Su veya süt ekle
if tercih.lower() == "su":
    kahve_makinesi.su_ekle(300)
elif tercih.lower() == "süt":
    kahve_makinesi.sut_ekle(300)    
else:
    kahve_makinesi.sut_ekle(300)

# Kahve ekle
kahve_makinesi.kahve_ekle(15)

# Kullanıcıya şekerli mi yoksa şekersiz mi tercih ettiğini sormak için:
sekerli_tercihi = input("Şekerli kahve mi yoksa şekersiz mi istersiniz? (şekerli/şekersiz): ")
if sekerli_tercihi.lower() == "şekerli":
    kahve_makinesi.kahve_hazirla(sekerli=True)
else:
    kahve_makinesi.kahve_hazirla()
