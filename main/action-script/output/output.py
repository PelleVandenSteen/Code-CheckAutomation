import time

def calculate_factorial(n):
    # Separating concerns by moving the validation to a separate function
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def validate_input(n):
    # Adjustment: Improved variable name for clarity
    if not isinstance(n, int):
        print("Input must be an integer.")
        return False
    return True

def print_factorial(n):
    if not validate_input(n):
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

#Adjustment-counter: 2