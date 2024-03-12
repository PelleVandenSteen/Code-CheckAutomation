import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    def power(self, base, exponent):
        # Adjustment: Improved power function using built-in exponentiation operator
        return base ** exponent

    def calculate_and_print_square_root(self, num):
        # Adjustment: Separated calculation and printing for square root
        self.result = math.sqrt(num)
        self.print_square_root(num)

    def print_square_root(self, num):
        # Adjustment: Added a separate method for printing square root
        print(f"The square root of {num} is {self.result}")

    def square(self, x):
        # Adjustment: Renamed 'sqare' method to 'square' for consistency
        return x * x

    def generate_random_numbers(self, count):
        # Adjustment: Improved variable naming for clarity
        random_numbers = [random.randint(1, 100) for _ in range(count)]
        return random_numbers

# Adjustment-counter: 4
