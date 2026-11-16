
# Discount Eligibility Checker

student = input("Are you a student? (yes/no): ").lower()
age = int(input("Enter your age: "))

# Either condition can qualify the customer
if student == "yes" or age >= 60:
    print("Congratulations! You qualify for a discount.")
else:
    print("Sorry, you do not qualify for a discount.")