'''
x =input("Enter first number:")
y =input("Enter second number:")

def add(x=3,y=4):
    print(int(x)+int(y))

def special():
    pass

add(x,y)
add(x)
add(3)
add(y=5)
add(y=5,x=6)

'''


# For lists 
# arbitary values
def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i
    print("Average is:",sum/len(numbers))


average(5,6)
average(5,6,7)
average(5,6,7,8)
average(5,6,7,8,9,10,12,14)


# For arbitary values of dictionary

def name(**name):
    print("Hello", name["fname"],name["mname"],name["lname"],)

name(mname="", fname="Aayush", lname="Dangi")