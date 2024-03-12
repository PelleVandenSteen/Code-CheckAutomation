
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print("The result is:", result)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(30)
print("Fibonacci number at position 30 is:", result)


def bbl_srt(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bbl_srt(arr)
print("Sorted array:", arr)


def calculate_area(length, breadth):
    return length * breadth

def calculate_perimeter(side1, side2):
    return 2 * (side1 + side2)

length = 5
breadth = 4
print("Area:", calculate_area(length, breadth))
print("Perimeter:", calculate_perimeter(length, breadth))


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

#we changin stuff