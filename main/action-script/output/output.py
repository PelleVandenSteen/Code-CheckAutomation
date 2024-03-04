import time

# Create a separate function to calculate factorial to adhere to separation of concerns principle
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Create a separate function to print factorial result for separation of concerns
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # Print the factorial result along with the time taken for calculation
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# Call the print_factorial function with input 5
print_factorial(5)


# Adjustments made: 2

# Adjustment-counter: 2
```