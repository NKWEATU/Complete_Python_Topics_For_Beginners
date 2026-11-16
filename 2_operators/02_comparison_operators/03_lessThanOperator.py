# Ask the user to enter their account balance
balance = int(input("Enter your account balance: "))

# Check if the account balance is less than 5000
if balance < 5000:
    # Display a warning if the balance is below 5000
    print("Warning! Your balance is low.")
else:
    # Display a message if the balance is 5000 or above
    print("Your balance is sufficient.")