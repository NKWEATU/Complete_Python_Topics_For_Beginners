# Create a shopping list
shopping = ["Rice", "Beans", "Oil", "Sugar"]

# Ask the user which item they want to remove
item = input("Enter the item to remove: ")

# Remove the specified item from the list
shopping.remove(item)

# Display the updated shopping list
print("Updated shopping list:", shopping)