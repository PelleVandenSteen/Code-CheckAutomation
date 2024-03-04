import time

def calculate_factorial(n):
    # Adjustment: Use a recursive approach for calculating factorial for a cleaner implementation
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def calculate_time_taken(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    time_taken = end_time - start_time
    return result, time_taken

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    result, time_taken = calculate_time_taken(calculate_factorial, n)

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)

# Adjustment-counter: 1