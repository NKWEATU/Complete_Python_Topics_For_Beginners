# Store the correct password
correct_password = "python123"

# Ask the user to enter a password
password = input("Enter your password: ")

# Continue asking while the password is incorrect
while password != correct_password:

    # Display an error message
    print("Incorrect password! Try again.")

    # Ask the user to enter the password again
    password = input("Enter your password: ")

# Display a success message
print("Access granted!")