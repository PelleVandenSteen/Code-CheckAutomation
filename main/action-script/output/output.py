import time

# Separation of concerns: Separate factorial calculation logic into its own function for better modularity
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

#Separation of concerns: Separate input validation and result printing for better modularity
def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    # Start time measurement
    start_time = time.time()
    
    # Calculate factorial
    result = calculate_factorial(n)
    
    # End time measurement
    end_time = time.time()

    # Output factorial result and time taken
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

#Adjustment-counter: 2