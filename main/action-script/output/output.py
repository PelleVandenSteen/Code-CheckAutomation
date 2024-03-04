import time

def calculate_factorial(n):
    # adjustment: Changed name of the variable for better clarity
    result = 1

    # Loop to calculate factorial
    for i in range(1, n + 1):
        result *= i

    return result

def validate_input(n):
    # adjustment: Added a separate function to validate input
    if not isinstance(n, int):
        print("Input must be an integer.")
        return None
    return n

def print_factorial(n):
    n = validate_input(n)
    if n is None:
        return

    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # adjustment: Included a separate function to print results
    print_results(n, result, end_time - start_time)

def print_results(n, result, time_taken):
    # adjustment: Improved output message for better readability
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)

#Adjustment-counter: 4