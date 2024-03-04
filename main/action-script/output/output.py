import time

def calculate_factorial(n):
    # improvement: added check for negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_and_measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return result, end_time - start_time

def print_factorial(n):
    # improvement: separated concerns by moving time measurement to a separate function
    result, time_taken = calculate_and_measure_time(calculate_factorial, n)

    # improvement: enhanced readability by using f-string for output formatting
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

print_factorial(5)

#Adjustment-counter: 3