import time

def calculate_factorial(n):
    # Adjustment: Changed the factorial calculation to use the built-in math function
    if n == 0:
        return 1
    import math
    return math.factorial(n)

def print_factorial(n):
    if not isinstance(n, int):
        # Adjustment: Improved error message for invalid input type
        print("Factorial can only be calculated for integers.")
        return
    
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    # Adjustment: Added timestamp to the output for better readability
    print(f"Calculation time: {end_time - start_time} seconds")

print_factorial(5)


#Adjustment-counter: 3