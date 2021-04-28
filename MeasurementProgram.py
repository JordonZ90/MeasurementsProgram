import measurements


def display_menu():
    print("MENU")
    print("1. Inches to Centimeters")
    print("2. Centimeters to inches")
    print("3. Feet to Yards")
    print("4. Yards to Feet")
    print("5. Feet to Miles")
    print("6. Miles to Feet")
    print("7. Miles to Kilometers")
    print("8. Kilometers to Miles")
    print()


def convert_measurements():
    option = int(input("Enter a menu option "))
    if option == 1:
        inches = float(input("Enter measurement in inches "))
        centimeters = measurements.inches_to_centimeters(inches)
        centimeters = round(centimeters, 2)
        print(f"Measurement in inches {inches} converted to {centimeters} centimeters")
    elif option == 2:
        centimeters = float(input("Enter measurement in centimeters "))
        inches = measurements.centimeters_to_inches(centimeters)
        inches = round(inches, 2)
        print(f"Measurement in centimeters {centimeters} converted to {inches} inches")
    elif option == 3:
        feet = float(input("Enter amount of feet "))
        yards = measurements.feet_to_yards(feet)
        yards = round(yards, 2)
        print(f"Measurement in feet {feet} converted to {yards} yards")
    elif option == 4:
        yards = float(input("Enter amount of yards "))
        feet = measurements.yards_to_feet(yards)
        feet = round(feet, 2)
        print(f"Measurement in yards {yards} converted to {feet} feet")
    elif option == 5:
        feet = float(input("Enter amount of feet "))
        miles = measurements.feet_to_miles(feet)
        miles = round(miles, 2)
        print(f"Measurement in feet {feet} converted to {miles} miles")
    elif option == 6:
        miles = float(input("Enter amount of miles "))
        feet = measurements.miles_to_feet(miles)
        feet = round(feet, 2)
        print(f"Measurement in miles {miles} converted to {feet} feet")
    elif option == 7:
        miles = float(input("Enter amount of miles "))
        kilometers = measurements.miles_to_kilometers(miles)
        kilometers = round(kilometers, 2)
        print(f"Measurement in miles {miles} converted to {kilometers} kilometers")
    elif option == 8:
        kilometers = float(input("Enter amount of kilometers "))
        miles = measurements.kilometers_to_miles(kilometers)
        miles = round(miles, 2)
        print(f"Measurement in kilometers {kilometers} converted to {miles} miles")
    else:
        print("Tou must enter a valid menu number")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_measurements()
        print()
        again = input("Convert another measurement? (y|n) ")
        if again == "y".lower():
            display_menu()
        else:
            print()
    print("Goodbye!")


if __name__ == "__main__":
    main()