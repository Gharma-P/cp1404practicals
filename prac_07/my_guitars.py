from guitar import Guitar

def main():
    guitars = []

    with open('guitars.csv', "r") as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))

    print("These are the guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("\nSorted guitars:")
    for guitar in guitars:
        print(guitar)

main()
