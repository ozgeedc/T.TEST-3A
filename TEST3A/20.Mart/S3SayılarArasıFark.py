# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.


print("\n *** We'll check which number is the biggest among three numbers you'll give \n")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

top_num = None

if num1 > num2 and num1 > num3:
    top_num = num1
    print ("The biggest number is your first number which is: ", top_num)
elif num2 > num1 and num2 > num3:
    top_num = num2
    print ("The biggest number is your second number which is: ", top_num)
elif num3 > num1 and num3 > num2:
    top_num = num3
    print ("The biggest number is your third number which is: ", top_num)
else:
    if num1 == num2 and num1 != num3:
        top_num = num1
        print ("You gave your first and second numbers as same \n Therefore they are both the biggest: ", top_num)
    elif num1 == num3 and num1 != num2:
        top_num = num1
        print ("You gave your first and third numbers as same \n Therefore they are both the biggest: ", top_num)
    elif num2 == num3 and num2 != num1:
        print ("You gave your second and third numbers as same \n Therefore they are both the biggest: ", top_num)
    else:
        top_num = num1
        print ("You gave all your numbers as same \n Therefore there can't be the biggest with these inputs...")

