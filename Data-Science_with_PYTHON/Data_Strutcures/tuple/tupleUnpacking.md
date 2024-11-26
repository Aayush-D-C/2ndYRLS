Tuple unpacking is a feature in Python that allows you to assign elements of a tuple (or any iterable) to multiple variables in a single operation. This is a convenient way to work with tuples, especially when they contain fixed data structures, such as coordinates, configurations, or multiple return values from a function.

Basic Example of Tuple Unpacking
python
Copy code
# A tuple with three elements
coordinates = (10, 20, 30)

# Unpacking the tuple into variables
x, y, z = coordinates

print("x =", x)  # Output: x = 10
print("y =", y)  # Output: y = 20
print("z =", z)  # Output: z = 30
Rules for Tuple Unpacking
The number of variables on the left side must match the number of elements in the tuple (or iterable).

python
Copy code
a, b = (1, 2)  # Correct
a, b, c = (1, 2)  # Error: not enough values to unpack
Use an asterisk (*) to unpack extra elements into a list.

python
Copy code
numbers = (1, 2, 3, 4, 5)

a, *b, c = numbers
print("a =", a)  # Output: a = 1
print("b =", b)  # Output: b = [2, 3, 4]
print("c =", c)  # Output: c = 5
Using Tuple Unpacking in Functions
Return Multiple Values from a Function
Functions in Python often return multiple values as a tuple. Tuple unpacking makes handling these results simple.

python
Copy code
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Unpacking the returned tuple
min_val, max_val, avg = calculate_stats([10, 20, 30, 40, 50])
print("Min:", min_val)  # Output: Min: 10
print("Max:", max_val)  # Output: Max: 50
print("Average:", avg)  # Output: Average: 30.0
Swapping Variables
Tuple unpacking can be used to swap variables without a temporary variable.

python
Copy code
a, b = 5, 10
a, b = b, a  # Swap the values
print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5
Nested Tuple Unpacking
You can unpack tuples inside tuples.

python
Copy code
nested_tuple = (1, (2, 3), 4)

a, (b, c), d = nested_tuple
print("a =", a)  # Output: a = 1
print("b =", b)  # Output: b = 2
print("c =", c)  # Output: c = 3
print("d =", d)  # Output: d = 4
Practical Applications
Iterating Over Enumerations:

python
Copy code
items = ["apple", "banana", "cherry"]
for index, value in enumerate(items):
    print(f"Index: {index}, Value: {value}")
Reading CSV or Structured Data:

python
Copy code
records = [("John", 25, "Engineer"), ("Jane", 30, "Doctor")]

for name, age, profession in records:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
Unpacking Function Arguments:

python
Copy code
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

person = ("Alice", 28)
greet(*person)  # Unpacks tuple into function arguments
