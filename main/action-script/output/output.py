import time

def calculate_factorial(n):
    #adjustment: Improved readability by removing unnecessary if condition
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def validate_input(n):
    #adjustment: Added a function to validate input and separate concerns
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

    #adjustment: Improved readability by using f-string for output formatting
    print(f"The factorial of {n} is: {result}")
    #adjustment: Improved readability by using f-string for output formatting
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

#Adjustment-counter: 4