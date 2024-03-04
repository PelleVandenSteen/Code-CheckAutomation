import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    def power(self, base, exponent):
        # Adjustment: Improved power function using built-in exponentiation operator
        return base ** exponent

    def calculate_and_print_square_root(self, num):
        self.result = math.sqrt(num)
        print(f"The square root of {num} is {self.result}")

    def square(self, x):
        # Adjustment: Renamed method sqare to square for consistency
        return x * x

    def generate_random_numbers(self, count):
        # Adjustment: Separated concerns, moved random number generation to a separate function
        return [random.randint(1, 100) for _ in range(count)]


# Adjustment-counter: 3