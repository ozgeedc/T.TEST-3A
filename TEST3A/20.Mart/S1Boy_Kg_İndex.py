# 1. 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

print("\n *** Let's see how fit you are...\n")
height = float(input("Please enter your height: \n"))
weight = float(input("Please enter your weight: \n"))
bmi = weight / (height ** 2)

print("Your body mass index is: ", bmi)

if bmi < 18.5:
    print ("Your weight is below ideal weight")
elif bmi >= 18.5 and bmi < 24.9:
    print ("Your weight is ideal")
elif bmi >= 25 and bmi < 29.9:
    print ("Your weight is above ideal weight")
elif bmi >= 30 and bmi < 39.9:
    print ("Your weight is dangerously above ideal weight. It's obese")
else:
    print ("Your weight is highly above ideal weight. It's morbidly obese")