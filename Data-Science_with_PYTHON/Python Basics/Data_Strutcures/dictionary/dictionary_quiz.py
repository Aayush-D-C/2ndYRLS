phone = input("Phone: ")

number = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
}

output =""

for i in phone:
       output += number.get(int(i),"NaN") + " "
     
print(output)

""""
    Output:
    Phone:12345 
    One Two Three Four NaN
"""