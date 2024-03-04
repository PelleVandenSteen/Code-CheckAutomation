import time

# Separated factorial calculation from printing for better separation of concerns
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Adjustment: Added type checking for input parameter n for better code reliability
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # Adjustment: Improved readability by using f-string for output
    print(f"The factorial of {n} is: {result}")
    # Adjustment: Added elapsed time calculation for performance evaluation
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

# Adjustment-counter: 3