# Define an examination result function
def calculate_average():

    # Ask the user to enter the first score
    score1 = float(input("Enter first score: "))

    # Ask the user to enter the second score
    score2 = float(input("Enter second score: "))

    # Ask the user to enter the third score
    score3 = float(input("Enter third score: "))

    # Calculate the average score
    average = (score1 + score2 + score3) / 3

    # Display the average
    print("Your average score is:", average)

# Call the function
calculate_average()