import random
import math

class ComplexCalculator:
    def __init__(self):
        self.result = 0

    #adjustment: Improved power function using built-in exponentiation operator
    def power(self, base, exponent):
        return base ** exponent

    def calculate_and_print_square_root(self, num):
        self.result = math.sqrt(num)
        print(f"The square root of {num} is {self.result}")

    #adjustment: Corrected method name from "sqare" to "square" for consistency
    def square(self, x):
        return x * x

    #adjustment: Separated random number generation logic into a dedicated method
    def generate_random_numbers(self, count):
        return [random.randint(1, 100) for i in range(count)]

#Adjustment-counter: 3
