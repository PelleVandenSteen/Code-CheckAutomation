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
        return x * x

    def generate_random_numbers(self, count):
        # Adjustment: Renamed variable for clarity
        random_numbers = []
        for _ in range(count):
            random_number = random.randint(1, 100)
            random_numbers.append(random_number)
        return random_numbers

# Adjustment-counter: 2
