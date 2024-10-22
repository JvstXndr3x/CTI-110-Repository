# Andrea Mejias
# 10/8/2024
# P2HW1
# This program calculates and displays travel expenses in a professional format

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
print(f"{'Location:':20} {travel_destination:<20}")
print(f"{'Initial Budget:':20} ${user_budget:<19.2f}")
print(f"{'Fuel:':20} ${gas_amount:<19.2f}")
print(f"{'Accomodation:':20} ${hotel_amount:<19.2f}")
print(f"{'Food:':20} ${food_amount:<19.2f}")
print("---------------------------------------")
print()
Remaining_Balance = user_budget - gas_amount - hotel_amount - food_amount
print(f"{'Remaining Balance:':20} ${Remaining_Balance:<19.2f}")

