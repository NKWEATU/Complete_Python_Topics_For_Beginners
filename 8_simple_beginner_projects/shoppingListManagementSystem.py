
# Shopping List Management System

# Create an empty shopping list
shopping_list = []

# Display the menu
while True:
    print("\n===== SHOPPING LIST MANAGEMENT SYSTEM =====")
    print("1. Add item")
    print("2. View shopping list")
    print("3. Remove item")
    print("4. Search for an item")
    print("5. Clear shopping list")
    print("6. Exit")

    # Ask the user to select an option
    choice = input("Enter your choice (1-6): ")

    # Option 1: Add an item
    if choice == "1":
        item = input("Enter the item you want to add: ")

        # Check that the item is not empty
        if item.strip() != "":
            shopping_list.append(item)
            print(item, "has been added successfully!")
        else:
            print("Please enter a valid item.")

    # Option 2: View all items
    elif choice == "2":
        print("\nYour Shopping List:")

        # Check if the list is empty
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            # Display each item with its number
            for index, item in enumerate(shopping_list, start=1):
                print(index, ".", item)

    # Option 3: Remove an item
    elif choice == "3":
        item = input("Enter the item you want to remove: ")

        # Check if the item exists in the list
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed successfully!")
        else:
            print("Item not found in your shopping list.")

    # Option 4: Search for an item
    elif choice == "4":
        item = input("Enter the item you want to search for: ")

        # Check whether the item exists
        if item in shopping_list:
            print(item, "is in your shopping list.")
        else:
            print(item, "is not in your shopping list.")

    # Option 5: Clear the shopping list
    elif choice == "5":
        shopping_list.clear()
        print("Your shopping list has been cleared.")

    # Option 6: Exit the program
    elif choice == "6":
        print("Thank you for using the Shopping List Management System!")
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Please select between 1 and 6.")
