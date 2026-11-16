# Ask the user to enter a starting number
number = int(input("Enter a starting number: "))

# Continue counting while the number is greater than zero
while number > 0:

    # Display the current number
    print(number)

    # Reduce the number by one
    number = number - 1

# Display a message when the countdown ends
print("Countdown completed!")