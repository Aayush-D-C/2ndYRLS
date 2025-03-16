numbers = [5,2,5,2,2]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "*"
    print(output)
    
"""
    1
    12
    123
    1234
    12345
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
