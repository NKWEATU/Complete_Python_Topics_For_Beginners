# Create a list of student names
# An IndexError occurs when you try to access a list position that does not exist.
students = ["John", "Mary", "Peter", "David"]

# Start the error handling block
try:

    # Ask the user to enter a list position
    position = int(input("Enter student position (0-3): "))

    # Display the student at the selected position
    print("Student name:", students[position])

# Handle invalid list positions
except IndexError:

    # Display an error message
    print("Error! That student position does not exist.")

# Handle non-numeric input
except ValueError:

    # Display an error message
    print("Error! Please enter a valid number.")