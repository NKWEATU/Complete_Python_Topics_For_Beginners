# A KeyError occurs when you try to access a dictionary key that does not exist.
# Create a dictionary of student names and scores
students = {
    "John": 75,
    "Mary": 85,
    "Peter": 65
}

# Start the error handling block
try:

    # Ask the user to enter a student's name
    name = input("Enter student name: ")

    # Display the student's score
    print("Student score:", students[name])

# Handle a name that does not exist in the dictionary
except KeyError:

    # Display an error message
    print("Error! Student not found.")