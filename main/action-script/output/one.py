def calc(operation, num1, num2):
    # Separated the calculation logic into individual functions for each operation
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        if num2 == 0:
            print('Cannot divide by zero.')
            return None
        return num1 / num2

    # Used a dictionary to map operations to their respective functions
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Check if the operation is valid
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        print('Invalid operation')
        return None

result1 = calc('add', 5, 3)
print('Result:', result1)
result2 = calc('divide', 10, 0)
print('Result:', result2)


#Adjustment-counter: 2