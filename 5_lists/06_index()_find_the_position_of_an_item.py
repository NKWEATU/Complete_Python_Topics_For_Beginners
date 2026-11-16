# Create a list of student names
students = ["John", "Mary", "Peter", "David"]

# Ask the user to enter a student's name
name = input("Enter student name to search: ")

# Find the position of the student
position = students.index(name)

# Display the student's position
print("Student position is:", position)