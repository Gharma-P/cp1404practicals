"""
Saves and overwrites list of guitars
"""
from guitar import Guitar
FILENAME = "guitars.csv"

def load_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars(filename, guitars):
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def display_guitars(guitars):
    for i, guitar in enumerate(guitars, start=1):
        print(f"{i}. {guitar}")


def add_new_guitars():
    new_guitars = []
    print("Enter new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars

def main():
    guitars = load_guitars(FILENAME)
    print("These are the current guitars")
    display_guitars(guitars)

    new_guitars = add_new_guitars()
    guitars.extend(new_guitars)

    guitars.sort()

    print("\nSorted Guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print("\nGuitars saved")

if __name__ == "__main__":
    main()

