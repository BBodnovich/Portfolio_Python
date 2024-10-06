def fibonacci(n):
    first = 0
    second = 1
    for _ in range(n+1):
        yield first
        next_fib = first + second
        first = second
        second = next_fib

current_number=0
for item in fibonacci(20):
    print(f'{current_number}\t{item}')
    current_number+=1
