# Your Name
# 11/11/2024
# P4HW2
# Display an employee's earnings by its pay and hours worked by using a while loop

# Ask for employee's name, hours worked, and pay rate, while also controlling the loop.
employee_name = input("Enter employee's name or Exit to terminate: ")

# Create incrementer variables
num_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0

# Use while loop to give the option to exterminate the program when asking for the employee name
while employee_name != "exit":
    num_employees += 1
    hours_worked = int(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    print()
    print("-------------------------------")
    # Do calculations first before displaying the information.
    # To determine overtime, subtract regular hours from the hours worked.
    overtime = hours_worked - 40
    if overtime < 0:
        overtime = 0
    overtime_pay = overtime * pay_rate
    regular_hours = hours_worked * pay_rate
    gross_pay = regular_hours + overtime_pay
    # Display information in a good format with all values as floats.
    print("Employee name: ", employee_name)
    print()
    print(f"{'Hours Worked':15} {'Pay Rate':15} {'OverTime':15} {'OverTime Pay':15} {'RegHour Pay':15} {'Gross Pay':15}")
    print("------------------------------------------------------------")
    print(f'{hours_worked:15} {pay_rate:15} {overtime:15} ${overtime_pay:<14.2f} ${regular_hours:<14.2f} ${gross_pay:<14.2f}')
    print()
    # Update the total variables in each loop.
    total_overtime += overtime_pay
    total_regular += regular_hours
    total_gross += gross_pay
    employee_name = input("Enter employee's name or Exit to terminate: ")

# Display information when user inputs the loop break.
print(f"Total number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")



