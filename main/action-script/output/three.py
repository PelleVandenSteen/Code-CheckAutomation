import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    #adjustment: Improved power function using built-in exponentiation operator
    def power(self, base, exponent):
        return base ** exponent

    #adjustment: Renamed method to calculate_and_print_square_root for clarity
    def calculate_and_print_square_root(self, num):
        self.result = math.sqrt(num)
        print(f"The square root of {num} is {self.result}")

    #adjustment: Fixed typo in method name from 'sqare' to 'square'
    def square(self, x):
        return x * x

    #adjustment: Extracted random number generation to a separate method for separation of concerns
    def generate_random_numbers(self, count):
        random_numbers = []
        for i in range(count):
            random_numbers.append(random.randint(1, 100))
        return random_numbers

#Adjustment-counter: 4
