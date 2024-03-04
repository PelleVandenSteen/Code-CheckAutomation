import time

def calculate_factorial(n):
    # Adjustment: Incorporated one-liner factorial calculation using `math.factorial` for improved performance
    from math import factorial
    return factorial(n)

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return

    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    # Adjustment: Improved readability by formatting the output message
    print(f"The factorial of {n} is: {result}")
    # Adjustment: Improved readability by formatting the time taken
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

#Adjustment-counter: 2