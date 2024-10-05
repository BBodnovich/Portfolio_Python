def fibonacci(number):
    answer = [0, 1]

    for i in range(2, number + 1):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer[number]


print(fibonacci(10))
