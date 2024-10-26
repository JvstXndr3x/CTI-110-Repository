# Your Name
# 10/24/20
# P5HW2
# Display an employee's earnings by its pay and hours worked

# Ask for employee's name, hours worked, and pay rate.
employee_name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print()
print("-------------------------------")
                 
# Do calculations first before displaying the information.
# To determine overtime, subtract regular hours from the hours worked.
overtime = hours_worked - 40
overtime_pay = overtime * pay_rate
regular_hours = 40 * pay_rate
gross_pay = regular_hours + overtime_pay

# Display information in a good format with all values as floats.
print("Employee name: ", employee_name)
print()
print(f"{'Hours Worked':15} {'Pay Rate':15} {'OverTime':15} {'OverTime Pay':15} {'RegHour Pay':15} {'Gross Pay':15}")
print("------------------------------------------------------------")
print(f"{hours_worked:15} {pay_rate:15} {overtime:15} ${overtime_pay:<14.2f} ${regular_hours:<14.2f} ${gross_pay:<14.2f}")
