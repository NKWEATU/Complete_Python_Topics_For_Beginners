# Set the initial total to zero
total = 0

# Ask the user to enter a number
number = int(input("Enter a number (0 to stop): "))

# Continue collecting numbers while the user does not enter zero
while number != 0:

    # Add the entered number to the total
    total = total + number

    # Ask the user to enter another number
    number = int(input("Enter another number (0 to stop): "))

# Display the sum of all entered numbers
print("The total sum is:", total)