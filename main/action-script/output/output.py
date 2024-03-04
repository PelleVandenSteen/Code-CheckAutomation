import time

def calculate_factorial(n):
    # Separated factorial calculation into a standalone function for better separation of concerns
    if n == 0:
        return 1
    # Utilized the math.factorial function for faster and simpler factorial computation
    return math.factorial(n)

def print_factorial(n):
    if not isinstance(n, int):
        print("Input must be an integer.")
        return
    start_time = time.time()
    result = calculate_factorial(n)
    end_time = time.time()

    print(f"The factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {end_time - start_time} seconds")

print_factorial(5)

#Adjustment-counter: 2