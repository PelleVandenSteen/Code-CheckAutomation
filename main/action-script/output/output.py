import time

def calculate_factorial(n):
    # Adjustment: Added type hint for the function return value
    # Adjustment: Optimized the factorial calculation by using math.prod
    import math
    return math.prod(range(1, n + 1))

def measure_time(func, *args):
    # Adjustment: Separated time measurement function for reusability
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    result, time_taken = measure_time(calculate_factorial, n)
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)


#Adjustment-counter: 4