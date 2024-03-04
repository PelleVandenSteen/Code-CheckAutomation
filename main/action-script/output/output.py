import time

def calculate_factorial(n):
    # Improvement: Handle edge case more explicitly and return 1 for n=0
    if n == 0:
        return 1
    
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def print_factorial(n):
    # Improvement: Check input type before proceeding
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # Improvement: Use f-string for better readability and avoid concatenation
    print(f"The factorial of {n} is: {result}")
    # Improvement: Calculate time taken within print statement for better separation of concerns
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)


#Adjustment-counter: 4