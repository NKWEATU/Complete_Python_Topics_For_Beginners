# Ask the user to enter 1 for Available or 0 for Not Available
computer = int(input("Is a computer available? (1 for Yes, 0 for No): "))

# Convert the input into a Boolean value
available = bool(computer)

# Display the availability status
print("Computer available:", available)