# Cinema Ticket Eligibility Checker

age = int(input("Enter your age: "))
money = float(input("How much money do you have? "))

# Both conditions must be true
if age >= 18 and money >= 2000:
    print("You are eligible to watch the movie!")
else:
    print("Sorry, you are not eligible.")