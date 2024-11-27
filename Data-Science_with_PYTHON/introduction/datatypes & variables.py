# ----------------------------------Data Types--------------------------------------------------
"""
This script covers the basic data types in Python:
1. Integer
2. Float
3. String
4. Boolean
5. Complex
"""

# Integer
intNumber = 3
print(intNumber)
print("The type of", intNumber, "is", type(intNumber))

# Float
decimate = 4.5
print(decimate)
print("The type of", decimate, "is", type(decimate))

# String
string = "Aayush"
print(string)
print("The type of", string, "is", type(string))

# Boolean
boolValue = True
print(boolValue)
print("The type of", boolValue, "is", type(boolValue))

# Complex Numbers
complexNum = 3 + 4j
print(complexNum)
print("The type of", complexNum, "is", type(complexNum))

# Type Conversion
# Converting between types
number = 10
print(float(number))  # Integer to float
print(str(number))    # Integer to string


#Use of fstring[formatted string literals]

first_name = "Alice"
print(f"My name is {first_name}");

#Formating Numbers

value = 1234.56789
print(f"Value with 2 decimals: {value:.2f}")
# Output: Value with 2 decimals: 1234.57

number = 1234567
print(f"Formatted number: {number:,}")
# Output: Formatted number: 1,234,567

# Multi-Line String
name = "Alice"
age = 25
info = f"""
Name: {name}
Age: {age}
"""
print(info)

'''
Advantages of f-strings
Readability: Easier to read and write compared to older formatting methods like .format() or %.
Performance: Faster than other string formatting techniques since it is evaluated at runtime.
'''