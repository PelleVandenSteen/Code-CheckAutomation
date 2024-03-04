import time

def calculate_factorial(n):
    # If n is 0 or 1, return 1 directly
    if n < 2:
        return 1

    # Initialize the factorial_result to 1
    factorial_result = 1

    # Calculate factorial iteratively
    for i in range(2, n + 1):
        factorial_result *= i

    return factorial_result

def print_factorial(n):
    # Check if n is an integer
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    
    # Record the start time for calculation
    start_time = time.time()

    # Call the calculate_factorial function to get the result
    result = calculate_factorial(n)

    # Record the end time after calculation
    end_time = time.time()

    # Display the factorial result and calculation time
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# Calculate and print the factorial of 5
print_factorial(5)

#Adjustment-counter: 2