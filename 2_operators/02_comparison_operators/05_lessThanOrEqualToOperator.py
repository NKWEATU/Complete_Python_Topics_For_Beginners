# Set the available budget
budget = 10000

# Ask the user to enter the price of the item
price = int(input("Enter the price of the item: "))

# Check if the item price is less than or equal to the budget
if price <= budget:
    # Display a message if the item is within the budget
    print("You can afford this item.")
else:
    # Display a message if the item is above the budget
    print("This item is above your budget.").")