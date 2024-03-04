import time

def calculate_factorial(n):
    # Adjustment: If n is 0, directly return 1
    if n == 0:
        return 1
    
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def calculate_time_taken(start_time, end_time):
    return end_time - start_time

def validate_input(n):
    # Adjustment: Improved error message clarity
    if not isinstance(n, int):
        print("Error: Input must be an integer.")
        return False
    return True

def print_factorial(n):
    if not validate_input(n):
        return
    
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    # Adjustment: Calculated time taken in separate function for clarity
    print(f"Time taken to calculate factorial: {calculate_time_taken(start_time, end_time)} seconds")

print_factorial(5)

# Adjustment-counter: 3