# Ask the student to enter 1 for Yes or 0 for No
registration = int(input("Have you completed registration? (1 for Yes, 0 for No): "))

# Convert the input into a Boolean value
status = bool(registration)

# Display the registration status
print("Registration completed:", status)