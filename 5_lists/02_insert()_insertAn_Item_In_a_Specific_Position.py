# Create a list of student names
students = ["John", "Mary", "Peter"]

# Ask the user to enter a student name
name = input("Enter a student name: ")

# Ask the user where to insert the name
position = int(input("Enter the position: "))

# Insert the name at the specified position
students.insert(position, name)

# Display the updated list
print("Updated student list:", students)