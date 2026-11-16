# Store the correct password
correct_password = "python123"

# Ask the user to enter their password
password = input("Enter your password: ")

# Check if the entered password matches the correct password
if password == correct_password:
    # Display a message if the password is correct
    print("Access granted!")
else:
    # Display a message if the password is incorrect
    print("Incorrect password!")