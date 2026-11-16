# A FileNotFoundError occurs 
# when a program tries to open a file that does not exist.
# Start the error handling block
try:

    # Ask the user to enter a filename
    filename = input("Enter the filename: ")

    # Attempt to open the file in read mode
    file = open(filename, "r")

    # Read the contents of the file
    content = file.read()

    # Display the file contents
    print(content)

    # Close the file
    file.close()

# Handle a file that does not exist
except FileNotFoundError:

    # Display an error message
    print("Error! The file does not exist.")