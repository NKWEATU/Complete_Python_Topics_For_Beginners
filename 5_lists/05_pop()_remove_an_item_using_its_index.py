# Create a list of student names
students = ["John", "Mary", "Peter", "David"]

# Ask the user to enter the position to remove
position = int(input("Enter the position to remove: "))

# Remove the student at the specified position
removed_student = students.pop(position)

# Display the removed student's name
print("Removed student:", removed_student)

# Display the updated list
print("Updated student list:", students)