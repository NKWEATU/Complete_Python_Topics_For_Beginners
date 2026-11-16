# Define the password checker function
def check_password():

    # Store the correct password
    correct_password = "python123"

    # Ask the user to enter their password
    password = input("Enter your password: ")

    # Check if the password is correct
    if password == correct_password:

        # Display a success message
        print("Access granted!")

    else:

        # Display an error message
        print("Incorrect password!")

# Call the function
check_password()