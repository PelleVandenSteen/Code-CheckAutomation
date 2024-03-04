import time

def calculate_factorial(n):
    # Calculating factorial for n
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_power(base, exponent):
    # Calculating power using exponentiation operator
    return base ** exponent

def print_factorial(n):
    # Printing the factorial and time taken
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# Adjustment-counter: 2


Adjusted code to include a separate function for calculating power using the exponentiation operator and added comments for clarity and readability.