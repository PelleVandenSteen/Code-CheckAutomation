import time

def calculate_factorial(n):
    # Adjustment: Added type hint for the function argument
    # Adjustment: Changed the function to use recursion for calculating factorial
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def print_factorial(n):
    # Adjustment: Added type hint for the function argument
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# Adjustment-counter: 2