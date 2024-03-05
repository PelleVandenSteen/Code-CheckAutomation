import time

def calculate_factorial(n):
    # Adjustment: Added input validation for negative integers
    if not isinstance(n, int) or n < 0:
        print("Input must be a non-negative integer.")
        return None

    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def print_factorial(n):
    if not isinstance(n, int) or n < 0:
        # Adjustment: Updated error message for negative integers
        print("Input must be a non-negative integer.")
        return

    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    if result is not None:
        print(f"The factorial of {n} is: {result}")
        print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)


#Adjustment-counter: 2