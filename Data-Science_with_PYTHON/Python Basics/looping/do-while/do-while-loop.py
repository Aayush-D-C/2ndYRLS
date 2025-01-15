'''

In Python, there is no construct defined for do while loop. Python loops only include for loop and while loop but we can modify the while loop to work as do while as in any other languages such as C++ and Java.

In Python, we can simulate the behavior of a do-while loop using a while loop with a condition that is initially True and then break out of the loop when the desired condition is met.

Do while loop
Do while loop is a type of control looping statement that can run any statement until the condition statement becomes false specified in the loop. In do while loop the statement runs at least once no matter whether the condition is false or true.

'''
x = input("Enter any number")

while(True):

    print(x)
    
    if(int(x)>2):
        x = input("Enter any number:")
    else:
        break
    
