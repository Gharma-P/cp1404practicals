"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit_conversion()
        elif choice == "F":
            celsius_conversion()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_conversion():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print(f"Result: {celsius:.2f} C")


def fahrenheit_conversion():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()