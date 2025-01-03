# ----------------------------------Lists in Python----------------------------------------
"""
This script demonstrates lists, which are mutable, ordered collections in Python.
"""

# Creating a List
l1 = ['1', 'hi', 'you', 'human']
print(l1)
print("Type of l1:", type(l1))

#To check inside a list a specific element
if 2 in l1:
    print("Yes")

# Accessing Elements
print("First element:", l1[0])
print("Last element:", l1[-1])
print("First three elements:", l1[0:3])
print(l1[:])

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

# To check if certain number is int he list or not
print(69 in l1)

#To copy the list in new list
l2 = l1.copy()
print("Copied list l1 to l2:",l2)

#clear the list 
l1.clear()
print(l1)


# List Operations
l2 = [3, 4, 5]
print("Concatenation:", l1 + l2)
print("Repetition:", l2 * 4)


#Largest in the list 
numbers  = [10,20,30,40,50]

largest = numbers[0]

for num in numbers:
    if(largest<num):
        largest = num

print(f"Largest Number is {largest}")

# 2D Lists  >> Very important for ML

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matrix[2][2])

# for row in matrix:
#     for item in row:
#         print(item)

#List Comprehension
lst = [i for i in range(5)]
print(lst)

lst = [i for i in range(10) if i%2==0]
print(lst)
