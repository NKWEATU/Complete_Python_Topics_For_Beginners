# Set the initial total to zero
total = 0

# Repeat the process five times
for i in range(1, 6):

    # Ask the user to enter a number
    number = int(input("Enter a number: "))

    # Add the entered number to the total
    total = total + number

# Display the final sum
print("The total sum is:", total)