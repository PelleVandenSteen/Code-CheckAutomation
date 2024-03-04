import time

# Separating concern by moving the factorial calculation to a separate function
def calculate_factorial(n):
    # Adjustment: Handling base case for factorial calculation
    if n == 0:
        return 1

    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i

    return factorial_result

# Separating concern by moving the printing functionality to a separate function
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # Adjustment: Improved readability by using f-string for output formatting
    print(f"The factorial of {n} is: {result}")
    # Adjustment: Improved readability by formatting time output
    print(f"Time taken to calculate factorial: {end_time - start_time:.6f} seconds")

# Calling the print_factorial function for a given input
print_factorial(5)

# Adjustment-counter: 4