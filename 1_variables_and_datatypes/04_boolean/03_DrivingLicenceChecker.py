# Ask the user to enter 1 for Yes or 0 for No
licence = int(input("Do you have a driving licence? (1 for Yes, 0 for No): "))

# Convert the input into a Boolean value
has_licence = bool(licence)

# Display the result
print("Has driving licence:", has_licence)