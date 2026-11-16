# Create an attendance list
attendance = ["John", "Mary", "John", "Peter", "John", "David"]

# Ask the user whose attendance they want to count
name = input("Enter student name: ")

# Count how many times the name appears
total = attendance.count(name)

# Display the attendance count
print(name, "appeared", total, "times.")