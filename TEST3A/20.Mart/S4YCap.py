# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)


print("\n *** We'll find out are and circumference of circle according to your radius input...\n ")
pi = 3.14159
radius = float(input("Please enter radius you like: "))
c_area = pi * (radius ** 2)
c_circumference = 2 * pi * radius
cal_message = f"\n Circle's area is: {c_area} \n Circle's circumference is: {c_circumference}\n"
print (cal_message)

