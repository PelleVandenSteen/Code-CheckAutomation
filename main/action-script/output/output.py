import time

def calculate_factorial(n):
    # Adjustment: Added type and value check for n
    if not isinstance(n, int) or n < 0:
        print("Factorial is defined for non-negative integers only.")
        return None
    
    if n == 0:
        return 1

    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_time_taken(start_time):
    end_time = time.time()
    return end_time - start_time

def print_factorial(n):
    # Adjustment: Improved function name for clarity
    start_time = time.time()

    result = calculate_factorial(n)

    if result is not None:
        print(f"The factorial of {n} is: {result}")
        # Adjustment: Used separate function for time calculation
        print(f"Time taken to calculate factorial: {calculate_time_taken(start_time)} seconds")

# Adjustment-counter: 3
