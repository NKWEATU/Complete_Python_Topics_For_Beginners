# Store the correct username and password
correct_username = "admin"
correct_password = "python123"

# Set the maximum number of attempts
attempts = 3

# Define the login function
def login():

    # Start the login attempt counter
    count = 0

    # Continue while attempts remain
    while count < attempts:

        # Ask the user to enter their username
        username = input("Enter username: ")

        # Ask the user to enter their password
        password = input("Enter password: ")

        # Check the login details
        if username == correct_username and password == correct_password:

            # Display a success message
            print("Login successful!")
            print("Welcome to the system.")

            # Stop the loop
            break

        else:

            # Increase the attempt counter
            count = count + 1

            # Calculate remaining attempts
            remaining = attempts - count

            # Display an error message
            print("Incorrect username or password.")

            # Display remaining attempts
            print("Attempts remaining:", remaining)

    # Check whether all attempts were exhausted
    if count == attempts:

        print("Account temporarily locked.")

# Call the login function
login()