import time

# Separated factorial calculation into its own function
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    start_time = time.time()
    
    # Utilized the calculate_factorial function for clarity and separation of concerns
    result = calculate_factorial(n)
    
    end_time = time.time()

    # Enhanced readability by formatting the output message
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)


#Adjustment-counter: 3