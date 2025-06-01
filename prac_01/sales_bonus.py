"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: "))
while sales >= 0:
    if sales < 1000:
        sales = sales * 0.1
        print(f"Sales Bonus: ${sales:.2f} ")

    elif sales >= 1000:
            sales = sales * 0.15
            print(f"Sales Bonus: ${sales:.2f} ")
            sales = float(input("Enter sales: "))

print("Error cannot be negative")












