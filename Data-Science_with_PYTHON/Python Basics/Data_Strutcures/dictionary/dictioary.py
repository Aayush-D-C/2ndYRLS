"""
Tricks to Remember:
    [] => List (Mutable, ordered)
    () => Tuple (Immutable, ordered)
    {} => Dictionary (Mutable, unordered key-value pairs) / Sets
"""

# Creating a Dictionary
Fruit = {
    "Apple": 10,    # Key: "Apple", Value: 10
    "Banana": 30    # Key: "Banana", Value: 30
}

# Display the dictionary and its type
print("Original Dictionary:", Fruit)
print("Type of Fruit:", type(Fruit))

# Accessing values using keys
print("Price of Apple:", Fruit["Apple"])

# Extracting Keys and Values
print("Keys:", Fruit.keys())    # Outputs all keys in the dictionary
print("Values:", Fruit.values()) # Outputs all values in the dictionary

# Adding a New Element
Fruit["Mango"] = 50
print("After Adding Mango:", Fruit)

# Modifying Existing Elements
Fruit["Apple"] = 100
Fruit["Banana"] = 60
print("After Modifying Apple and Banana:", Fruit)

# Dictionary Update Method
# Adding another dictionary to the existing one
fruit2 = {
    "Guava": 40,
    "Orange": 90
}
Fruit.update(fruit2)
print("After Updating with a Second Dictionary:", Fruit)

# Removing an Element using `pop()`
Fruit.pop("Banana")  # Removes the key "Banana"
print("After Removing Banana:", Fruit)

#Nested Dictionary
nested_dict = {
    "Fruit": {"Apple": 10, "Banana": 30},
    "Vegetables": {"Carrot": 20, "Potato": 15}
}
print(nested_dict["Fruit"]["Apple"])  # Output: 10
