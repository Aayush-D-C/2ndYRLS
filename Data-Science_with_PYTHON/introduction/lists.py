# ----------------------------------Lists in Python----------------------------------------
"""
This script demonstrates lists, which are mutable, ordered collections in Python.
"""

# Creating a List
l1 = ['1', 'hi', 'you', 'human']
print(l1)
print("Type of l1:", type(l1))

# Accessing Elements
print("First element:", l1[0])
print("Last element:", l1[-1])
print("First three elements:", l1[0:3])

# Modifying a List
l1.append("Aayush")  # Add an element to the end
print("After appending:", l1)

l1.pop()  # Remove the last element
print("After popping:", l1)

l1.reverse()  # Reverse the list
print("After reversing:", l1)

l1.insert(3, "Dangi")  # Insert at a specific position
print("After inserting 'Dangi':", l1)

l1.sort()  # Sort the list
print("After sorting:", l1)

# List Operations
l2 = [3, 4, 5]
print("Concatenation:", l1 + l2)
print("Repetition:", l2 * 4)
