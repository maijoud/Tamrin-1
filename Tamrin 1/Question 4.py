def convert_temperature():
    print(" Temperature Converter")
    print("Please choose the direction of conversion:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    try:
        choice = int(input("Enter your choice (1/2): "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return

    if choice == 1:
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    elif choice == 2:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        fahrenheit = (celsius * 9.0 / 5.0) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    else:
        print("Invalid choice. Please choose either 1 or 2.")


convert_temperature()
