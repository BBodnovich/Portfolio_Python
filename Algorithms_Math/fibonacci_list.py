def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 2] + fib_numbers[i - 1])
    return fib_numbers[n]

print(fibonacci(10))
