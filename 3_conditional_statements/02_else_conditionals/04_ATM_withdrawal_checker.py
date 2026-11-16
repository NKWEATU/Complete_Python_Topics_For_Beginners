
# ATM Withdrawal Checker

# Ask the user for their account balance
balance = float(input("Enter your account balance: "))

# Ask the user for the withdrawal amount
withdrawal = float(input("Enter withdrawal amount: "))

# Check if the balance is enough
if balance >= withdrawal:
    remaining_balance = balance - withdrawal
    print("Withdrawal successful!")
    print("Your remaining balance is:", remaining_balance)
else:
    print("Insufficient balance!")
