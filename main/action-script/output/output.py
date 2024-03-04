import time

# Separating the calculation of factorial into a standalone function for improved separation of concerns
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result

# Renamed the function to better reflect its purpose
def compute_and_print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # Output the result
    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

# Calling the function with the desired input
compute_and_print_factorial(5)


#Adjustment-counter: 4