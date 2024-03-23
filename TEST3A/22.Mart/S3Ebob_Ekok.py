def ebob(a, b):
    while b: # ne zaman 0 olursa dur
        print (f"\n a, b: {a}, {b} \n")
        a, b = b, a % b
    return a

def ekok(a, b):
    print("a x b: ", a * b)
    return (a * b) // ebob(a, b)


a = int(input("\n first_number: "))
b = int(input("\n second_number: ")) 

print(f"ebob({a}, {b}) = {ebob(a, b)}")
print(f"ekok({a}, {b}) = {ekok(a, b)}")