import time

def calculate_factorial(n):
    # Improvement: Use a recursive function for factorial calculation
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def measure_time_taken(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    result, time_taken = measure_time_taken(calculate_factorial, n)

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)


#Adjustment-counter: 2
```