def fibonacci(n):
    a, b = 1, 1
    fibonacci_list = [a, b]
    for i in range(n - 2):
        a, b = b, a + b
        fibonacci_list.append(b)
    return fibonacci_list

print(fibonacci(20))