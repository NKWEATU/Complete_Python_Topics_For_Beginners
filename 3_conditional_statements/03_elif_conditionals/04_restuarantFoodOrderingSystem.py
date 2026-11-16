
# Restaurant Food Ordering System

# Display the available meals
print("WELCOME TO OUR RESTAURANT")
print("1. Rice")
print("2. Beans")
print("3. Chicken")
print("4. Pizza")

# Ask the user to select a meal
choice = int(input("Choose a meal (1-4): "))

# Check the selected meal
if choice == 1:
    print("You selected Rice.")
    print("Price: N3000")

elif choice == 2:
    print("You selected Beans.")
    print("Price: N2000")

elif choice == 3:
    print("You selected Chicken.")
    print("Price: N5000")

elif choice == 4:
    print("You selected Pizza.")
    print("Price: N7000")

else:
    print("Invalid food selection!")
