import time

def calculate_factorial(n):
    if n < 0:  # adjustment: Guard clause for negative input
        return "Factorial is not defined for negative numbers."
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_time_taken(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return result, end_time - start_time

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    result, time_taken = calculate_time_taken(calculate_factorial, n)
    
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken:.6f} seconds")  # adjustment: Limited decimal points in time output

print_factorial(5)


#Adjustment-counter: 4