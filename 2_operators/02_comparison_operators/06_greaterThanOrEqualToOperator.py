# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check if the user's age is greater than or equal to 18
if age >= 18:
    # Display a message if the user is 18 or older
    print("You are eligible to watch this movie.")
else:
    # Display a message if the user is below 18
    print("You are too young to watch this movie.")