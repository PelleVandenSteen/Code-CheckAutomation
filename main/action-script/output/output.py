import time

def calculate_factorial(n):
    # Improvement: Validate input
    if not isinstance(n, int) or n < 0:
        print("Factorial is defined for non-negative integers only.")
        return None

    if n == 0:
        return 1

    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

def print_factorial(n):
    # Improvement: Use separate function for calculating time
    result, time_taken = calculate_time(calculate_factorial, n)

    if result is not None:
        print(f"The factorial of {n} is: {result}")
        print(f"Time taken to calculate factorial: {time_taken} seconds")

# Adjustment: Improved handling of non-integer input
print_factorial(5)

# Adjustment-counter: 2
