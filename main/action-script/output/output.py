import time

# Separation of concerns: Create a separate function to calculate factorial
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Separation of concerns: Create a separate function to print factorial and measure time
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

#Adjustment-counter: 2