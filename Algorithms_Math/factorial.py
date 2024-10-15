def find_factorial(number):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    number (int): A non-negative integer

    Returns:
    int: Factorial of given number
    """

    # Input Validation Checks
    if number < 0:
        raise ValueError("Negative numbers not supported")

    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    # Factorial Algorithm
    if number == 0:
        return 1

    answer = 1
    for i in range(2, number + 1):
        answer *= i
    return answer

print(find_factorial(10))
