
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:  # number 1'den küçük veya eşitse, bu sayının asal olup olmadığını belirtmek için false 
            return False
    return True # Eğer yukarıda ki koşul sağlanmazsa True

number = 0 # Asal değildir.
number = 19 # Asaldır.


#Asal sayı kontrolü yapar ve çıktı oluşturur.
if is_prime(number):
    print(f"{number} Asaldir")
else:
    print(f"{number} Asal degildir")
