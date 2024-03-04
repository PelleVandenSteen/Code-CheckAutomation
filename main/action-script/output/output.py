import time

def calculate_factorial(n):
    # Adjustment: Added docstring to describe the function
    """
    Calculate the factorial of a given number.

    Arguments:
    n -- an integer

    Returns:
    factorial_result -- the factorial of the input number
    """
    if n == 0:
        return 1
    
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    
    return factorial_result

def print_factorial(n):
    # Adjustment: Added docstring to describe the function
    """
    Print the factorial of a given number and the time taken to calculate it.

    Arguments:
    n -- an integer

    Prints:
    The factorial of the input number
    Time taken to calculate the factorial
    """
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# Adjustment-counter: 2

