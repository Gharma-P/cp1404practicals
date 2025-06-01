"""
Work out total price for the number of items, each with different prices
Program allows users to enter the number of items and the price
Then, program computes and displays the total price of those items
If the total price of those items is over $100, then a 10% discount is applied to that total
before the amount is displayed on screen
"""
# get number of items
# get price of each item
# if price > 100 then 10% discount applied
# print total cost

total_price = 0
number_of_items = int(input("Number of items: "))

#Error-checking for invalid input
while True:
    if number_of_items < 0:
        print("Invalid number of items")
        number_of_items = int(input("Number of items: "))
    else:
        break

for i in range(0, number_of_items, 1):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price = total_price - (total_price * 0.10)
    print(f"Total price: ${total_price:.2f}")
else:
    print(f"Total price: ${total_price:.2f}")


