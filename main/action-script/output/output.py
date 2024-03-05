import time

# Separating concerns: Create a function to calculate factorial
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Improvement: Rename the function to be more descriptive
def calculate_and_print_factorial(n):
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()
    
    return result, end_time - start_time

# Separating concerns: Create a function to handle input validation and printing
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    result, time_taken = calculate_and_print_factorial(n)
    
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {time_taken} seconds")

# Call the function to calculate and print factorial for input 5
print_factorial(5)


#Adjustment-counter: 3