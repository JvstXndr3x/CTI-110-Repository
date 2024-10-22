# Andrea Mejias
# 10/22/2024
# P3LAB
# Calculate coin combinations of a given price value

# Regular Division
#print(100/3)

# Floor Division - Returns the whole number.
#print(100//3)

# Modulus Division - Return the remainder as an integer.
#print(100%3)
#print(7%4)

money = float(input("Enter the amount of money as a float: $"))

money = round(money * 100)

#print(money)

numberofdollars = money // 100
print(f"Dollars: {numberofdollars}")

money = money - (numberofdollars * 100)

numberofquarters = money // 25
print(f"Quarters: {numberofquarters}")

money = money - (numberofquarters * 25)

numberofdimes = money // 10
print(f"Dimes: {numberofdimes}")

money = money - (numberofdimes * 10)

numberofnickels = money // 5
print(f"Nickels: {numberofnickels}")

money = money - (numberofnickels * 5)

numberofpennies = money
print(f"Pennies: {numberofpennies}")
