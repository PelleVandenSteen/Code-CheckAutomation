import time

def calculate_factorial(n):
    # Adjustment: Included a docstring to describe the function
    """
    Calculate the factorial of a given integer.
    
    Parameters:
    n (int): The integer for which factorial will be calculated.
    
    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def print_factorial(n):
    # Adjustment: Included a docstring to describe the function
    """
    Print the factorial of a given integer along with the time taken for calculation.
    
    Parameters:
    n (int): The integer for which factorial will be printed.
    """
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time:.6f} seconds")  # Adjustment: Added formatting for time

print_factorial(5)


#Adjustment-counter: 4