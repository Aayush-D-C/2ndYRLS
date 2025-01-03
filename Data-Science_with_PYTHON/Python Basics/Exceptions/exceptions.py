while True:
    try:
        age = int(input("Enter your age: "))

        income = 200000
        risk = income / age

        print(f"Your age is {age}")
        print(f"Your risk of income is {risk}")
        break

    except ValueError:
        print("❌ Invalid input detected! Please enter a valid integer for your age.")

    except ZeroDivisionError:
        print(f"❌ Provided age 0 detected | Cannot divide .")
