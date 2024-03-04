import time

def calculate_factorial(n):
    # Adjustment: Changed iterative calculation to use built-in functions for performance
    return 1 if n == 0 else n * calculate_factorial(n - 1)

def calculate_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    result, time_taken = calculate_execution_time(calculate_factorial, n)
    
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)

#Adjustment-counter: 2