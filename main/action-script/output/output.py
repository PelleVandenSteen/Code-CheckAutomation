import time

def calculate_factorial(n):
    """
    This function calculates the factorial of a given integer.
    """
    if n == 0:
        return 1

    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_and_measure_factorial(n):
    """
    This function calculates the factorial of a given integer and measures the time taken.
    """
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()
    
    return result, end_time - start_time

def print_factorial(n):
    """
    This function prints the factorial of a given integer along with the time taken to calculate it.
    """
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    result, time_taken = calculate_and_measure_factorial(n)

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)

# Adjustment-counter: 3