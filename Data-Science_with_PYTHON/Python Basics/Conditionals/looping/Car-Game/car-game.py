import random

car_started = False  # Tracks whether the car is started
fuel_level = 100  # Initial fuel level
status_message = "Car is stopped."

while True:
    command = input("> ").lower()

    if command == "help":
        print('''
        Commands:
            start - Start the car
            stop - Stop the car
            drive - Drive the car
            status - Check the car's status
            fuel - Refuel the car
            quit - Quit the game
        ''')

    elif command == "start":
        if car_started:
            print("The car is already started!")
        else:
            car_started = True
            status_message = "Car is running."
            print("Car started...Ready to go!")

    elif command == "stop":
        if not car_started:
            print("The car is already stopped!")
        else:
            car_started = False
            status_message = "Car is stopped."
            print("Car stopped.")

    elif command == "drive":
        if not car_started:
            print("You need to start the car first!")
        elif fuel_level <= 0:
            print("No fuel! Refuel the car before driving.")
        else:
            fuel_consumption = random.randint(10, 30)
            if fuel_level >= fuel_consumption:
                fuel_level -= fuel_consumption
                print(f"You drive around and consume {fuel_consumption} units of fuel.")
            else:
                fuel_level = 0
                print("You tried to drive, but the car ran out of fuel!")

    elif command == "fuel":
        if fuel_level < 100:
            fuel_level = 100
            print("Car refueled! Fuel level is now full.")
        else:
            print("The car already has a full tank of fuel.")

    elif command == "status":
        print(f"Status: {status_message}")
        print(f"Fuel level: {fuel_level}")

    elif command == "quit":
        confirm = input("Are you sure you want to quit? (yes/no): ").lower()
        if confirm == "yes":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Resuming the game...")

    else:
        print("Beep Beep Boop | Can't Understand the command")
