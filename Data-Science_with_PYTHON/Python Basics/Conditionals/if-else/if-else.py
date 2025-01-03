is_hot = False
is_cold = True

is_notcold = True

temperature = 40

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")

# elif is_cold:
#     print("It's a cold day")

# else:
#     print("Enjoy your day")

# Logical Operator
# if is_hot and is_notcold:
#     print("It's a hot day")
#     print("Drink plenty of water")

# else:
#     print("Enjoy your day")

# if is_cold and not is_hot:
#     print("Enjoy your day")

# if temperature >= 40:
#     print("You have a fever")

print("Form Validation\n")
name = input("Enter your name:")

if len(name)<3:
    print("!Name cannot be less than 3 letters!\n")

elif len(name)>50:
    print("!Too long for name!\n")

else:
    print("Login Successfull")