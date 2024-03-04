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
        random_numbers_list = []
        for _ in range(count):
            # Adjustment: Changed randint to randrange for continuous range
            random_numbers_list.append(random.randrange(1, 101))
        return random_numbers_list

# Adjustment-counter: 2
