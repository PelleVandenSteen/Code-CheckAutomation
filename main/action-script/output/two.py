# Adjustment: Improved function name to be more descriptive
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print("The result is:", result)


# Adjustment: Added memoization to improve performance
fibonacci_cache = {}
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        fibonacci_cache[n] = result
        return result

result = fibonacci(30)
print("Fibonacci number at position 30 is:", result)


# Adjustment: Improved function name for better readability
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)


# Adjustment: Added docstrings for functions to enhance readability
def calculate_area(length, breadth):
    """Calculate the area of a rectangle."""
    return length * breadth

def calculate_perimeter(side1, side2):
    """Calculate the perimeter of a rectangle."""
    return 2 * (side1 + side2)

length = 5
breadth = 4
print("Area:", calculate_area(length, breadth))
print("Perimeter:", calculate_perimeter(length, breadth))


# Adjustment: Separated Calculator and PrintResult classes for separation of concerns
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class PrintResult:
    def print(self, result):
        print("The result is:", result)

calculator = Calculator()
print_result = PrintResult()
result = calculator.add(3, 4)
print_result.print(result)

# Adjustment-counter: 7
