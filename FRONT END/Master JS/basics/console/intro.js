// Console methods
console.log("Hello World!"); // Prints a message to the console
console.error("Undefined Error"); // Prints an error message
console.clear(); // Clears the console window

// Operators

// Arithmetic operators
var firstNumber = 4;
var secondNumber = 5;
var multiply = firstNumber * secondNumber;
var addition = firstNumber + secondNumber;
var subtraction = firstNumber - secondNumber;
var division = firstNumber / secondNumber;
var modulus = firstNumber % secondNumber; // Remainder of division
var exponentiation = firstNumber ** secondNumber; // Exponentiation (4^5) or simply use math 

console.log("Multiply:", multiply);
console.log("Addition:", addition);
console.log("Subtraction:", subtraction);
console.log("Division:", division);
console.log("Modulus:", modulus);
console.log("Exponentiation:", exponentiation);

var power = Math.pow(4,5);
console.log("The power of 4^5 is:",power);

// Relational Operators
console.log("5 > 2:", 5 > 2);  // Greater than
console.log("5 < 2:", 5 < 2);  // Less than
console.log("5 >= 2:", 5 >= 2); // Greater than or equal to
console.log("5 <= 2:", 5 <= 2); // Less than or equal to
console.log("5 == 2:", 5 == 2); // Equal to
console.log("5 != 2:", 5 != 2); // Not equal to
console.log("5 === 5:", 5 === 5); // Strict equality (checks type and value)
console.log("5 !== '5':", 5 !== "5"); // Strict inequality

// Logical Operators
var isAdult = true;
var hasLicense = false;

console.log("isAdult AND hasLicense:", isAdult && hasLicense); // AND operator
console.log("isAdult OR hasLicense:", isAdult || hasLicense); // OR operator
console.log("NOT isAdult:", !isAdult); // NOT operator

// Bitwise Operators
var a = 4876;
var right_shifted_by_3 = a >> 3; // Right shift
var left_shifted_by_2 = a << 2; // Left shift
var bitwise_and = a & 3; // Bitwise AND
var bitwise_or = a | 3; // Bitwise OR
var bitwise_xor = a ^ 3; // Bitwise XOR
var bitwise_not = ~a; // Bitwise NOT

console.log("Right-Shifted by 3:", right_shifted_by_3);
console.log("Left-Shifted by 2:", left_shifted_by_2);
console.log("Bitwise AND:", bitwise_and);
console.log("Bitwise OR:", bitwise_or);
console.log("Bitwise XOR:", bitwise_xor);
console.log("Bitwise NOT:", bitwise_not);

// typeof Operator
// Determines the type of a variable
var number =5;
var string = `Aayush`;    // (``) USe of template literal
var boolean = true;

var vehicle={
    brand_name :"Ford",
    tyre_type : "OE",
    mileage: "60mpl"
};

console.log("Type of number:", typeof number); // number
console.log("Type of string:", typeof string); // string
console.log("Type of boolean:", typeof boolean); // boolean
console.log("Type of object:", typeof vehicle); // object

// Additional data types
// 1. Undefined
var notAssigned;
console.log("Type of notAssigned:", typeof notAssigned); // undefined

// 2. Null
var emptyValue = null;
console.log("Type of emptyValue:", typeof emptyValue); // object (quirk of JavaScript)

// Ternary (Conditional) Operator
// A short form for conditional (if-else) statements
var age = 18;
var canVote = age >= 18 ? "Yes" : "No";
console.log("Can vote:", canVote);

// Assignment Operators
var x = 10;
x += 5; // Equivalent to x = x + 5
console.log("After += 5:", x);

x -= 3; // Equivalent to x = x - 3
console.log("After -= 3:", x);

x *= 2; // Equivalent to x = x * 2
console.log("After *= 2:", x);

x /= 4; // Equivalent to x = x / 4
console.log("After /= 4:", x);

x %= 3; // Equivalent to x = x % 3
console.log("After %= 3:", x);

x **= 2; // Equivalent to x = x ** 2
console.log("After **= 2:", x);

// Special Operators
// 1. typeof: returns the type of a variable (as shown above)
// 2. delete: removes a property from an object
delete vehicle.tyre_type;
console.log("After delete vehicle.tyre_type:", vehicle);

// 3. in: checks if a property exists in an object
console.log("mileage in vehicle:", "mileage" in vehicle); // true

// 4. instanceof: checks if an object is an instance of a specific class or prototype
console.log("vehicle instanceof Object:", vehicle instanceof Object); // true

// Practice Exercise
// Simple program to check if a number is even or odd using the modulus operator
var numberToCheck = 9;
var isEven = (numberToCheck % 2 == 0) ? "Even" : "Odd";
console.log("Number is:", isEven);
