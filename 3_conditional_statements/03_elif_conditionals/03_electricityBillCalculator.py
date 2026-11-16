
# Electricity Bill Calculator

# Ask the user for electricity units
units = float(input("Enter units consumed: "))

# Calculate the bill based on consumption
if units <= 100:
    bill = units * 50
    print("Your bill is:", bill)

elif units <= 200:
    bill = units * 75
    print("Your bill is:", bill)

elif units <= 300:
    bill = units * 100
    print("Your bill is:", bill)

else:
    bill = units * 120
    print("Your bill is:", bill)
