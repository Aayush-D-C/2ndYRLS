# Arithmetic Operators
a, b = 10, 3
print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation
print(f"a // b = {a // b}")  # Floor Division

print("\nComparison Operators:")
# Comparison Operators
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a > b: {a > b}")    # Greater than
print(f"a < b: {a < b}")    # Less than
print(f"a >= b: {a >= b}")  # Greater than or equal to
print(f"a <= b: {a <= b}")  # Less than or equal to

print("\nAssignment Operators:")
# Assignment Operators
x = 5
print(f"x = {x}")
x += 2  # x = x + 2
print(f"x += 2 -> x = {x}")
x -= 1  # x = x - 1
print(f"x -= 1 -> x = {x}")
x *= 3  # x = x * 3
print(f"x *= 3 -> x = {x}")
x /= 2  # x = x / 2
print(f"x /= 2 -> x = {x}")
x %= 3  # x = x % 3
print(f"x %= 3 -> x = {x}")
x //= 2  # x = x // 2
print(f"x //= 2 -> x = {x}")
x **= 2  # x = x ** 2
print(f"x **= 2 -> x = {x}")

print("\nLogical Operators:")
# Logical Operators
p, q = True, False
print(f"p and q: {p and q}")  # Logical AND
print(f"p or q: {p or q}")    # Logical OR
print(f"not p: {not p}")      # Logical NOT

print("\nBitwise Operators:")
# Bitwise Operators
m, n = 5, 3  # Binary: 5 = 0101, 3 = 0011
print(f"m & n: {m & n}")  # Bitwise AND
print(f"m | n: {m | n}")  # Bitwise OR
print(f"m ^ n: {m ^ n}")  # Bitwise XOR
print(f"~m: {~m}")        # Bitwise NOT
print(f"m << 1: {m << 1}")  # Left Shift
print(f"m >> 1: {m >> 1}")  # Right Shift

print("\nMembership Operators:")
# Membership Operators
lst = [1, 2, 3, 4]
print(f"2 in lst: {2 in lst}")  # Membership test
print(f"5 not in lst: {5 not in lst}")  # Membership test

print("\nIdentity Operators:")
# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(f"x is y: {x is y}")  # True (same object)
print(f"x is z: {x is z}")  # False (different objects with same content)
print(f"x is not z: {x is not z}")  # True

print("\nSpecial Operators:")
# Ternary Operator
max_value = a if a > b else b
print(f"Ternary operator: max_value = {max_value}")

# Chained Operators
print(f"Chained operators: 5 < a <= 15 -> {5 < a <= 15}")

# Walrus Operator (Python 3.8+)
if (length := len(lst)) > 3:
    print(f"Walrus operator: Length of list = {length}")
