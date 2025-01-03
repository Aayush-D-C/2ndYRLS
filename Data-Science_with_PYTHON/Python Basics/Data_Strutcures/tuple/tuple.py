"""
Program: Tuple Operations in Python
Author: [Your Name]
Description:
    This script demonstrates the creation and manipulation of tuples in Python.
    It covers basic tuple operations like indexing, slicing, concatenation, 
    repetition, and using built-in functions like `max()` and `min()`.
"""

# -------------------------- Tuple Basics --------------------------

# Creating a tuple
tup1 = (1, "Aayush", True, 3, 4, "Dangi")

# Display the entire tuple
print("Tuple 1:", tup1)

# Accessing elements in the tuple using indexing
print("Element at index 2:", tup1[2])  # Access the third element (True)
print("Last element:", tup1[-1])  # Access the last element ("Dangi")

# Slicing the tuple (from index 0 to 4, excluding index 5)
print("Sliced tuple (0 to 5):", tup1[0:5])

# Finding the length of the tuple
print("Length of Tuple 1:", len(tup1))

# -------------------------- Tuple Operations --------------------------

# Creating another tuple for operations
tup2 = (6, 9)

# Concatenation: Combining two tuples
print("Concatenated Tuple:", tup1 + tup2)

# Repetition: Repeating a tuple multiple times
print("Repeated Tuple:", tup1 * 3)

# Combining repetition and concatenation
print("Repeated Tuple + Second Tuple:", tup1 * 3 + tup2)

# -------------------------- Built-in Functions --------------------------

# Finding the maximum and minimum values in a numeric tuple
print("Maximum value in Tuple 2:", max(tup2))
print("Minimum value in Tuple 2:", min(tup2))

# -------------------------- Additional Examples --------------------------

# Demonstrating immutability
# Uncommenting the next line will raise an error because tuples are immutable
# tup1[0] = 100  

# Tuple with mixed data types
tup_mixed = ("Python", 3.14159, [1, 2, 3], False)
print("Mixed Tuple:", tup_mixed)

# Nested tuple
nested_tup = (tup1, tup2)
print("Nested Tuple:", nested_tup)

# Tuple unpacking
a, b = tup2
print("Unpacked Tuple 2: a =", a, ", b =", b)

# A tuple with three elements
coordinates = (10, 20, 30)

# Unpacking the tuple into variables
x, y, z = coordinates

print("x =", x)  # Output: x = 10
print("y =", y)  # Output: y = 20
print("z =", z)  # Output: z = 30

numbers = (1, 2, 3, 4, 5)

a, *b, c = numbers
print("a =", a)  # Output: a = 1
print("b =", b)  # Output: b = [2, 3, 4]
print("c =", c)  # Output: c = 5




# Using the `count` and `index` methods
tup3 = (1, 2, 2, 3, 4, 2, 5)
print("Count of 2 in Tuple 3:", tup3.count(2))  # Count occurrences of 2
print("Index of 3 in Tuple 3:", tup3.index(3))  # Find the index of the first occurrence of 3

#To find the index of 2 in tup3
print(tup3.index(2))

# Converting a list to a tuple
list_example = [10, 20, 30]
converted_tuple = tuple(list_example)
print("Converted Tuple from List:", converted_tuple)

# Converting a tuple back to a list
converted_list = list(converted_tuple)
print("Converted List from Tuple:", converted_list)
