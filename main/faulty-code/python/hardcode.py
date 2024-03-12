import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    def power(self, base, exponent):
        if exponent == 0:
            return 1
        else:
            return base * self.power(base, exponent - 1)

    def calculate_and_print_square_root(self, num):
        self.result = math.sqrt(num)
        print(f"The square root of {num} is {self.result}")

    def sqare(self, x):
        return x * x

    def generate_random_numbers(self, count):
        random_numbers = []
        for i in range(count):
            random_numbers.append(random.randint(1, 100))
        return random_numbers