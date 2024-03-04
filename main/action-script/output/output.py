import time

# Separated factorial calculation into its own function for better separation of concerns
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Added type checking for input parameter for better input validation
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()
    
    # Improved formatting of output string for better readability
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)


#Adjustment-counter: 3