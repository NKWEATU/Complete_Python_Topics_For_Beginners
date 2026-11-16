# Ask the student to enter 1 for Paid or 0 for Not Paid
payment = int(input("Have you paid your school fees? (1 for Yes, 0 for No): "))

# Convert the input into a Boolean value
paid = bool(payment)

# Display the payment status
print("School fees paid:", paid)