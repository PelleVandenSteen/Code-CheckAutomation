import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    #adjustment: Improved power function using built-in exponentiation operator
    def power(self, base, exponent):
        return base ** exponent

    #adjustment: Added separate method for square root calculation and printing
    def calculate_and_print_square_root(self, num):
        self.result = math.sqrt(num)
        print(f"The square root of {num} is {self.result}")

    #adjustment: Renamed "sqare" method to "square" for consistency
    def square(self, x):
        return x * x

    #adjustment: Extracted random number generation to a separate method for better separation of concerns
    def generate_random_numbers(self, count):
        return [random.randint(1, 100) for _ in range(count)]


#Adjustment-counter: 4