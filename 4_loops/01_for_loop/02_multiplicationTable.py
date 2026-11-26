# Ask the user to enter a number
number = int(input("Enter a number: "))

# Generate the multiplication table from 1 to 10
for i in range(1, 12):
    # Multiply the number by the current value of i
    result = number * i

    # Display the multiplication result
    print(number, "x", i, "=", result)