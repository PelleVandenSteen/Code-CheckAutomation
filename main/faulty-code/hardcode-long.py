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


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def calculate_and_print_circumference(radius):
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle with radius {radius} is {circumference}")


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def concatenate_strings(string_list):
    result = ""
    for s in string_list:
        result += s
    return result


calc = ComplexCalculator()
calc.calculate_and_print_square_root(25)
print("Random numbers:", calc.generate_random_numbers(5))
print("Factorial:", factorial(5))
print("Sorted list:", bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
calculate_and_print_circumference(5)
print("Index of 4 in the list:", linear_search([1, 2, 3, 4, 5], 4))
print("Concatenated string:", concatenate_strings(["Hello", " ", "World"]))
