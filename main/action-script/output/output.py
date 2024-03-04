import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    def power(self, base, exponent):
        """Calculate and return the power of a base to an exponent."""
        return base ** exponent

    def calculate_and_print_square_root(self, num):
        """Calculate the square root of a number and print the result."""
        self.result = math.sqrt(num)
        print(f"The square root of {num} is {self.result}")

    def square(self, x):
        """Calculate and return the square of a number."""
        return x * x

    def generate_random_numbers(self, count):
        """Generate a list of random numbers within a specified range."""
        random_numbers = [random.randint(1, 100) for _ in range(count)]
        return random_numbers

#Adjustment-counter: 4
