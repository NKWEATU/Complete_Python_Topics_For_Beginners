# Ask the user to enter the starting number
start = int(input("Enter starting number: "))

# Ask the user to enter the ending number
end = int(input("Enter ending number: "))

# Count numbers using for loop
for number in range(start, end + 1):
    print(number)