def primeOrNot(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def findPrimeFactors(number):
    if number < 2:
        return False
    prime_factors = []
    i = 1
    while i < number:
        if number % i == 0 and primeOrNot(i):
            prime_factors.append(i)
        i += 1
    if primeOrNot(number):
        prime_factors.append(number)
    return prime_factors

# Kullanıcıdan sayı girişi al ve asal bölenleri bul
number = int(input("Bir sayı girin: "))
prime_factors = findPrimeFactors(number)
if not prime_factors:
    print("Geçersiz sayı veya asal bölen yok.")
else:
    print(f"{number} sayısının asal bölenleri: {prime_factors}")