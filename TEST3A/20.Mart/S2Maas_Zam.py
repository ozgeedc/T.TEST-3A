
#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.


print("\n *** Let's how your new salary is satisfied for you...\n")

salary = int(input("Please enter your monthly salary: \n"))
raise_rate = float(input("Please enter the last salary increase you received: \n"))

current_salary = salary + (salary * (raise_rate / 100))

hr_message = f"Your current salary is: {current_salary} \n if it seems like low please knock on your boss's door \n Otherwise, we wish you happiness until the next hike period..."

print(hr_message)