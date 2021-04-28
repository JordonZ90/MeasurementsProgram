import moremeasurements


def display_menu():
    print("MENU")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print()


def convert_measurements():
    option = int(input("Enter a menu option "))
    if option == 1:
        kilometers = float(input("Enter measurement in kilometers "))
        meters = moremeasurements.kilometers_to_meters(kilometers)
        meters = round(meters, 2)
        print(f"Measurement in kilometers {kilometers} converted to {meters} meters")
    elif option == 2:
        meters = float(input("Enter measurement in meters "))
        kilometers = moremeasurements.meters_to_kilometers()
        kilometers = round(kilometers, 2)
        print(f"Measurement in meters {meters} converted to {kilometers} kilometers")
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
