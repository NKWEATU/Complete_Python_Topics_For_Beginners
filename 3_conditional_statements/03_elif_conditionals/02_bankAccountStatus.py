
# Bank Account Status Checker

# Ask the user to enter their balance
balance = float(input("Enter your account balance: "))

# Check the account balance
if balance >= 1000000:
    print("Account Status: VIP Customer")

elif balance >= 500000:
    print("Account Status: Premium Customer")

elif balance >= 100000:
    print("Account Status: Standard Customer")

elif balance >= 0:
    print("Account Status: Basic Customer")

else:
    print("Invalid account balance!")
