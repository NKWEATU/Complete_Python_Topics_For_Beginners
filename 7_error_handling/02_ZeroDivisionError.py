# Start the error handling block
# A ZeroDivisionError occurs when a program attempts to divide a number by zero.
try:

    # Ask the user to enter the first number
    num1 = int(input("Enter the first number: "))

    # Ask the user to enter the second number
    num2 = int(input("Enter the second number: "))

    # Divide the first number by the second number
    result = num1 / num2

    # Display the result
    print("The answer is:", result)

# Handle division by zero
except ZeroDivisionError:

    # Display an error message
    print("Error! You cannot divide by zero.")