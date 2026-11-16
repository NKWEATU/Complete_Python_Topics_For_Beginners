
# Shopping Payment Checker

# Ask the user for the price of an item
price = float(input("Enter item price: "))

# Ask the user how much money they have
money = float(input("Enter your available money: "))

# Check if the customer has enough money
if money >= price:
    change = money - price
    print("Payment successful!")
    print("Your change is:", change)
else:
    shortage = price - money
    print("Insufficient money!")
    print("You need an additional:", shortage)
