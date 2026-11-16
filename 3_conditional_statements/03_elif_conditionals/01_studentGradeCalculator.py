
# Student Grade Calculator

# Ask the student to enter their score
score = int(input("Enter your score: "))

# Check the score and assign a grade
if score >= 80:
    print("Grade A - Excellent!")

elif score >= 70:
    print("Grade B - Very Good!")

elif score >= 60:
    print("Grade C - Good!")

elif score >= 50:
    print("Grade D - Pass!")

else:
    print("Grade F - Failed!")
