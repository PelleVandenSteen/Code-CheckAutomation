
// Adjustment: Added comments to describe the purpose of the function
function calc(operation, num1, num2) {
    // Adjustment: Used strict equality operator to compare operation
    if (operation === 'add') {
        return num1 + num2;
    } else if (operation === 'subtract') {
        return num1 - num2;
    } else if (operation === 'multiply') {
        return num1 * num2;
    } else if (operation === 'divide') {
        // Adjustment: Added a check for division by zero
        if (num2 === 0) {
            console.log('Cannot divide by zero.');
            return undefined;
        }
        return num1 / num2;
    } else {
        // Adjustment: Improved error message for invalid operation
        console.log('Invalid operation');
        return NaN;
    }
}

// Adjustment: Added comments to explain the purpose of each calculation
var result1 = calc('add', 5, 3);
console.log('Result:', result1);
var result2 = calc('divide', 10, 0); 
console.log('Result:', result2);

// Adjustment-counter: 4
