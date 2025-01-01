# --------------------------------
# Python Data Structures: Sets
# --------------------------------

# A set is a collection of unique, unordered, and mutable elements.

# Example of Creating a Set
set1 = {3, "a",True, 2, "b", False}  # A mixed set containing integers, strings, and booleans
print("Initial Set:", set1)  # Output may vary due to the unordered nature of sets

# Adding an Element
set1.add("HELLO")  # Adds the string "HELLO" to the set
print("After Adding 'HELLO':", set1)

# Removing an Element
set1.remove("b")
set1.remove(True)

print("After Removing 'b' and True:", set1)

# Adding Multiple Elements
# The update() method can add multiple elements from an iterable, ensuring only unique items are added.
set1.update([10, 20, 10, 20])  # Adding numbers 10 and 20 (duplicates are ignored)
print("After Adding Multiple Elements:", set1)

# --------------------------------
# Set Operations: Union and Intersection
# --------------------------------

# Defining two sets for operations
set3 = {1, 2, 3, 4}
set4 = {3, 4, "a", "A"}

# Union of sets: Combines all unique elements from both sets
union_result = set3.union(set4)
print("Union of set3 and set4:", union_result)  # Output: {1, 2, 3, 4, 'a', 'A'}

# Intersection of sets: Retrieves common elements
intersection_result = set3.intersection(set4)
print("Intersection of set3 and set4:", intersection_result)  # Output: {3, 4}
