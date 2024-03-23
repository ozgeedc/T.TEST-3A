# 5-Kullanıcıdan alınan bir sayının ya da metnin palindrom olup olmadığını bulan bir program yazınız.

print("\n *** We'll find out if your number/word is palindrome or not...\n ")
while True:
    sample = input("Your number or word please: ")

    if sample.isdigit():
        reversed_sample = sample[::-1]
        if reversed_sample == sample:
            print("Yes, it's a palindrome.")
        else:
            print("Unfortunately, it's not a palindrome.")
        break
    elif sample.isalpha():
        reversed_sample = sample[::-1].lower()
        if reversed_sample == sample.lower():
            print("Yes, it's a palindrome.")
        else:
            print("Unfortunately, it's not a palindrome.")
        break
    else:
        print("Please enter only numbers or only letters. Try again.")