# Andrea Mejias
# 10/03/2024
# P2LAB2
# Creating a program that creates a dictionary of usable keys and values

# Create the dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Get the keys
keys = cars.keys()
print(keys)
print()

# Prompt user to give one of the keys
userchoice = input("Enter a vehicle to see it's mpg: ")
print()

# Show user mpg for their selected car
print(f"The {userchoice} gets {cars[userchoice]} mpg.")
print()

# get amount of miles to be driven
miles_driven = float(input(f"How many miles will you drive the {userchoice}? "))
print()

# Calculate the gallons needed to drive miles assigned
required_gallons = miles_driven/cars[userchoice]

# Display gallons needed to user
print(f"{required_gallons:.2f} gallons of gas are needed to drive the {userchoice}.")


