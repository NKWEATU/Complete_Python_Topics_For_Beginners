# Define the salary calculator function
def calculate_salary():

    # Start error handling
    try:

        # Ask for the employee's name
        name = input("Enter employee name: ")

        # Ask for the daily salary
        daily_salary = float(input("Enter daily salary: "))

        # Ask for the number of days worked
        days = int(input("Enter number of days worked: "))

        # Calculate the total salary
        total_salary = daily_salary * days

        # Display employee salary information
        print("\nEMPLOYEE SALARY REPORT")
        print("Employee Name:", name)
        print("Daily Salary:", daily_salary)
        print("Days Worked:", days)
        print("Total Salary:", total_salary)

    # Handle invalid number inputs
    except ValueError:

        print("Error! Please enter valid numbers.")

# Call the salary calculator function
calculate_salary()