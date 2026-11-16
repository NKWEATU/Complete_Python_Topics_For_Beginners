# Ask how many student names the user wants to enter
total = int(input("How many students? "))

# Repeat the process based on the total number of students
for i in range(1, total + 1):

    # Ask the user to enter a student's name
    name = input("Enter student name: ")

    # Display the student's name
    print("Student", i, ":", name)