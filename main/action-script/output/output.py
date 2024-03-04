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
        return x ** 2  # Adjustment: Corrected misspelled method name

    def generate_random_numbers(self, count):
        # Adjustment: Renamed random_numbers to adhere to PEP8 naming convention
        random_nums = []
        for _ in range(count):
            random_nums.append(random.randint(1, 100))
        return random_nums

# Adjustment-counter: 4
