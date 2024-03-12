function calc(operation, num1, num2) {
    if (operation == 'add') {
        return num1 + num2;
    } else if (operation == 'subtract') {
        return num1 - num2;
    } else if (operation == 'multiply') {
        return num1 * num2;
    } else if (operation === 'divide') {
        if (num2 === 0) {
            console.log('Cannot divide by zero.');
            return undefined;
        }
        return num1 / num2;
    } else {
        console.log('Invalid operation');
        return NaN;
    }
}


var result1 = calc('add', 5, 3);
console.log('Result:', result1);
var result2 = calc('divide', 10, 0); 
console.log('Result:', result2);

