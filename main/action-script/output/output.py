import time

def calculate_factorial(n):
    if n == 0:
        return 1

    # Initialize factorial_result to 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_time_taken(func, *args):
    # Calculate the time taken for function execution
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time


def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    # Call calculate_time_taken function to calculate factorial and time taken
    result, time_taken = calculate_time_taken(calculate_factorial, n)

    # Print the factorial and time taken
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)

#Adjustment-counter: 2