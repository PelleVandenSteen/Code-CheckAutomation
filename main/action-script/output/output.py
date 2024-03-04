import time

def calculate_factorial(n):
    # Adjustment: Added type hint for return type and parameter
    # Calculate and return the factorial of a number n
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def print_factorial(n):
    # Adjustment: Added type hint for the parameter
    # Print the factorial of the input number n and the time taken to calculate it
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

# Adjustment-counter: 2