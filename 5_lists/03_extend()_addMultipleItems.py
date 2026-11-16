# Create an existing shopping list
shopping = ["Rice", "Beans", "Oil"]

# Ask the user to enter three new items
item1 = input("Enter first item: ")
item2 = input("Enter second item: ")
item3 = input("Enter third item: ")

# Create a list of the new items
new_items = [item1, item2, item3]

# Add all the new items to the shopping list
shopping.extend(new_items)

# Display the updated shopping list
print("Shopping list:", shopping)