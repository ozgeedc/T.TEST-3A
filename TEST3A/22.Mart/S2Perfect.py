def findPerfectNumber(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    if total == number:
        print("it's a perfect number")
    else:
        print("it's not a perfect number")


findPerfectNumber(int(input("Enter a number..: ")))