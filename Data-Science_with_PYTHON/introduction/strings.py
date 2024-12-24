# ------------------------------Strings in Python----------------------------------------
"""
This script demonstrates the properties and methods of strings in Python.

String is immutable
"""

# String Declarations
str1 = "Aayush"
str2 = 'Aayush'
str3 = '''A
          a
          y
          u
          s
          h'''

print(str1)
print(str2)
print(str3)

# String Properties
strExample = "Hello World"

# Accessing Characters
print("Last character using negative indexing:", strExample[-1])
print("Length of the string:", len(strExample))

# String Methods
print("Uppercase:", strExample.upper())
print("Lowercase:", strExample.lower())

# Replace
print("Replace 'World' with 'Human':", strExample.replace("World", "Human"))

# Find
print("Find position of 'World':", strExample.find("World"))

# Splitting a String
# Splits into a list of substrings
strSentence = "The spark of creativity is yours; we are merely the tools to bring it to life."
print("Split on ';':", strSentence.split(';'))

blogHeading = "introduction TO flask"
print(blogHeading.capitalize())

print(blogHeading.center(21))

double = " hello  hello"
print(double.count("hello"))

print(double.endswith("hello"))

print(double.isprintable())
print(double.isspace())
print(strSentence.istitle())