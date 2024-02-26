import time

def calculate_factorial(n):
    # Adjustment: Changed the function to use recursion for a clearer implementation
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def calculate_execution_time(start_time):
    # Adjustment: Separated time calculation into a new function for separation of concerns
    end_time = time.time()
    return end_time - start_time

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
 
    start_time = time.time()
    result = calculate_factorial(n)
    execution_time = calculate_execution_time(start_time)

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {execution_time} seconds")

print_factorial(5)

# Adjustment-counter: 2