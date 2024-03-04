import time

def calculate_factorial(n):
    """
    Calculates the factorial of a given integer.
    Args:
        n: int, input integer
    Returns:
        int, factorial result
    """
    if n == 0:
        return 1
    
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
        
    return factorial_result

def print_factorial(n):
    """
    Prints the factorial of a given integer and the time taken to calculate it.
    Args:
        n: int, input integer
    """
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)


# Adjustment-counter: 0