# Ask the user to enter their examination score
score = int(input("Enter your exam score: "))

# Check if the examination score is greater than 50
if score > 50:
    # Display a congratulatory message if the score is above 50
    print("Congratulations! You passed.")
else:
    # Display a message if the score is 50 or below
    print("You did not score above 50.")