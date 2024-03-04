import time

# improvement: Moved factorial calculation to a separate function for better separation of concerns
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# improvement: Introduced input validation to ensure the input is an integer
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # improvement: Improved readability by formatting the output messages
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# improvement: Added a call to print_factorial with argument 5 for demonstration
print_factorial(5)


#Adjustment-counter: 6
```