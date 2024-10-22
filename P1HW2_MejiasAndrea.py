# Andrea Mejias
# 9/19/2024
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses.")
print()
user_budget = int(input("Enter Budget: "))
print()
travel_destination = input("Enter your travel destination: ")
print()
gas_amount = int(input("How much do you think you will spend on gas? "))
print()
hotel_amount = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food_amount = int(input("Last, how much do you need for food? "))
print()
print("------------Travel Expenses------------")
print("Location:", travel_destination)
print("Initial Budget:", user_budget)
print()
print("Fuel:", gas_amount)
print("Accomodation:", hotel_amount)
print("Food:", food_amount)
print()
Remaining_Balance = user_budget - gas_amount - hotel_amount - food_amount
print("Remaining Balance:", Remaining_Balance)

