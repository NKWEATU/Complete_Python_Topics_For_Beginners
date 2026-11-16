# Age calculator
# A ValueError occurs when a user enters 
# a value that cannot be converted into the required data type.
# Start the error handling block
try:

    # Ask the user to enter their age
    age = int(input("Enter your age: "))

    # Display the user's age
    print("Your age is:", age)

# Handle an invalid number input
except ValueError:

    # Display an error message
    print("Error! Please enter a valid number.")