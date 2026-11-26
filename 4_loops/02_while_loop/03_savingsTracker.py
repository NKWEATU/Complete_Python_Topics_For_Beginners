# Ask the user to enter their current savings
savings = int(input("Enter your current savings: "))

# Continue adding money while savings are below 5000
while savings < 5000:

    # Add 1000 to the current savings
    savings = savings + 1000

    # Display the updated savings
    print("Your savings is now:", savings)

# Display a message when the target is reached
print("Congratulations! You have reached your savings target.")