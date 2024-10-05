def find_factorial(number):
    if number < 0:
        raise ValueError("Negative numbers not supported")
    if number == 0:
        return 1
    answer = 1
    for i in range(2, number + 1):
        answer *= i
    return answer

print(find_factorial(10))
