Python Data Structures: Lists, Tuples, and Dictionaries
Overview
This document covers the basic concepts, properties, and examples of three fundamental data structures in Python:

Lists: Ordered, mutable collections.
Tuples: Ordered, immutable collections.
Dictionaries: Key-value pair collections.
1. Lists
Definition
A list is a collection of items that is:

Ordered: Maintains the insertion order of elements.
Mutable: You can add, modify, or remove elements.
Syntax
python
Copy code
list_name = [item1, item2, item3, ...]
Example
python
Copy code
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")  # Add an item
fruits[0] = "Strawberry"  # Modify the first item
print(fruits)  # Output: ['Strawberry', 'Banana', 'Cherry', 'Mango']
Common Operations
Operation	Example	Output
Add an item	fruits.append("Mango")	['Apple', 'Banana', 'Cherry', 'Mango']
Remove an item	fruits.remove("Banana")	['Apple', 'Cherry']
Access an item	fruits[0]	'Apple'
Slicing	fruits[1:3]	['Banana', 'Cherry']
2. Tuples
Definition
A tuple is a collection of items that is:

Ordered: Maintains the insertion order.
Immutable: Once created, its elements cannot be changed.
Syntax
python
Copy code
tuple_name = (item1, item2, item3, ...)
Example
python
Copy code
coordinates = (10, 20, 30)
print(coordinates[0])  # Output: 10
# coordinates[0] = 15  # This will raise an error because tuples are immutable.
Common Operations
Operation	Example	Output
Access an item	coordinates[1]	20
Length of a tuple	len(coordinates)	3
Concatenate tuples	(1, 2) + (3, 4)	(1, 2, 3, 4)
3. Dictionaries
Definition
A dictionary is a collection of key-value pairs that is:

Unordered: Does not guarantee the order of keys (but preserves insertion order from Python 3.7 onwards).
Mutable: Keys and values can be added, modified, or removed.
Syntax
python
Copy code
dict_name = {key1: value1, key2: value2, ...}
Example
python
Copy code
fruit_prices = {"Apple": 100, "Banana": 60}
fruit_prices["Mango"] = 50  # Add a new key-value pair
fruit_prices["Apple"] = 120  # Modify the value of "Apple"
print(fruit_prices)  # Output: {'Apple': 120, 'Banana': 60, 'Mango': 50}
Common Operations
Operation	Example	Output
Access a value	fruit_prices["Apple"]	100
Add/Update a value	fruit_prices["Mango"] = 50	Adds/updates 'Mango': 50
Remove a key-value	fruit_prices.pop("Banana")	Removes "Banana"
Get keys	fruit_prices.keys()	dict_keys(['Apple', 'Mango'])
Get values	fruit_prices.values()	dict_values([120, 50])
Comparison Table
Feature	List	Tuple	Dictionary
Definition	Ordered, mutable collection	Ordered, immutable collection	Key-value mapping
Syntax	[item1, item2]	(item1, item2)	{key1: value1}
Mutability	Mutable	Immutable	Mutable
Duplicates	Allows duplicates	Allows duplicates	Keys are unique, values can duplicate
Access Method	Indexing (list[0])	Indexing (tuple[0])	By key (dict['key'])
When to Use
Lists:

When you need an ordered, modifiable collection.
Example: Storing a sequence of tasks or items.
Tuples:

When you need an ordered, fixed collection.
Example: Storing constant values like coordinates or days of the week.
Dictionaries:

When you need to map keys to values for quick lookups.
Example: Storing product prices, user information, or configurations.
License
This documentation is provided as-is for educational purposes.