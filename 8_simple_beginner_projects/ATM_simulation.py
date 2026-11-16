# Set the initial account balance
balance = 10000

# Define the ATM function
def atm():

    # Access the account balance
    global balance

    # Keep displaying the ATM menu
    while True:

        # Display available options
        print("\nWELCOME TO PYTHON ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Ask the user to select an option
        choice = input("Select an option: ")

        # Check the user's selection
        if choice == "1":

            # Display account balance
            print("Your balance is:", balance)

        elif choice == "2":

            # Ask for the deposit amount
            amount = int(input("Enter deposit amount: "))

            # Add the deposit to the balance
            balance = balance + amount

            # Display the updated balance
            print("New balance:", balance)

        elif choice == "3":

            # Ask for the withdrawal amount
            amount = int(input("Enter withdrawal amount: "))

            # Check whether sufficient funds are available
            if amount <= balance and amount > 0:

                # Deduct the withdrawal from the balance
                balance = balance - amount

                # Display the updated balance
                print("Withdrawal successful!")
                print("New balance:", balance)

            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "4":

            # Exit the ATM program
            print("Thank you for using our ATM.")
            break

        else:

            # Handle an invalid menu selection
            print("Invalid option. Try again.")

# Call the ATM function
atm()