# Ask the user to enter the student's name
name = input("Enter student name: ")

# Create an empty list for examination scores
scores = []

# Collect three examination scores
for i in range(1, 4):
    score = float(input("Enter examination score: "))

    # Add each score to the list
    scores.append(score)

# Calculate the total score
total = sum(scores)

# Calculate the average score
average = total / 3

# Display the student's information
print("\nSTUDENT RESULT")
print("Student Name:", name)
print("Total Score:", total)
print("Average Score:", average)

# Check whether the student passed or failed
if average >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")