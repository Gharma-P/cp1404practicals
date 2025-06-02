"""
Scores Menu
"""

def main():
    # name = "Gharma Peniyamina"
    score = 0
    print("Menu")
    choice = input(">").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            pass
        elif choice == "P":
            print_score(score)
            pass
        elif choice == "S":
            print_stars(score)
            pass
        else:
            print("Invalid Choice")
        print("Menu:")
        choice = input(">").upper()
    print("Farewell")


def print_score(score):
    print(get_valid_score(score))

def get_valid_score(score):
    if score < 0 or score > 100:
        return "Error"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

def print_stars(score):
    print('*' * score)

main()

