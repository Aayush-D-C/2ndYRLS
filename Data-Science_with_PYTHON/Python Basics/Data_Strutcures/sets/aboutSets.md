Python Data Structures: Sets
Overview
A set is a built-in data structure in Python that:

Stores unique elements: Duplicate values are not allowed.
Is unordered: The elements have no defined order and cannot be accessed by indexing.
Is mutable: You can add or remove elements.
Basic Set Operations
Creating a Set
python
Copy code
set1 = {1, "a", True, 2, "b", False}
print(set1)  # Output: {False, 1, 2, 'b', 'a'}
Adding an Element
python
Copy code
set1.add("HELLO")
print(set1)  # Output: {False, 1, 2, 'b', 'a', 'HELLO'}
Removing an Element
Using remove:

python
Copy code
set1.remove("b")
print(set1)  # Output: {False, 1, 2, 'a', 'HELLO'}
Removing Booleans: Boolean values (True and False) are part of sets but are considered equivalent to 1 and 0. Use their integer equivalents to remove them:

python
Copy code
set1.remove(True)  # Removes the value `True`
print(set1)        # Output: {False, 2, 'a', 'HELLO'}
Adding Multiple Elements
python
Copy code
set1.update([10, 20, 10, 20])  # Adds only unique values
print(set1)  # Output: {False, 2, 10, 20, 'a', 'HELLO'}
Set Functions
Union and Intersection
Union: Combines all unique elements from two sets.

python
Copy code
set3 = {1, 2, 3, 4}
set4 = {3, 4, "a", "A"}
print(set3.union(set4))  # Output: {1, 2, 3, 4, 'a', 'A'}
Intersection: Retrieves only the common elements.

python
Copy code
print(set3.intersection(set4))  # Output: {3, 4}
Key Points About Sets
Unique Elements: Sets automatically remove duplicate entries.

python
Copy code
example_set = {1, 2, 2, 3}
print(example_set)  # Output: {1, 2, 3}
No Indexing: Sets do not support indexing or slicing as they are unordered.

python
Copy code
set_example = {1, 2, 3}
# print(set_example[0])  # Raises an error
Immutability of Elements: Set elements must be immutable (e.g., strings, numbers, tuples). Mutable objects like lists cannot be added to a set.

Removing Elements Safely: Use discard instead of remove if you’re unsure whether an element exists, as discard won’t raise an error:

python
Copy code
set1.discard("nonexistent")  # No error raised
Example Code
python
Copy code
# Creating a set
my_set = {1, 2, 3, 4}
print("Original Set:", my_set)

# Adding elements
my_set.add(5)
print("After Adding 5:", my_set)

# Removing elements
my_set.remove(2)
print("After Removing 2:", my_set)

# Multiple additions
my_set.update([10, 20])
print("After Adding Multiple Elements:", my_set)

# Union and Intersection
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
