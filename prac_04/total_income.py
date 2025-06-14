"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def get_number_of_months(incomes, months):
    for number_of_months in range(1, months + 1):
        income = float(input(f"Enter income for month {number_of_months}: "))
        incomes.append(income)

def income_report(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for number_of_months in range(1, months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10,.2f} Total: ${:10,.2f}".format(number_of_months, income, total))
        # added comma for thousands separator

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))
    get_number_of_months(incomes, months)
    income_report(incomes, months)

main()
