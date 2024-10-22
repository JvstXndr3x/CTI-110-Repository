# Andrea Mejias
# 9/17/2024
# P1HW1
# Input and output with mathematical expressions

print("-----Calculating Exponents-----")
print()
print()
# Get base value (as an integer) from the user
baseValue = int(input("Enter an integer as the base value: "))

# Get exponent value from user
exponent = int(input("Enter an integer as the exponent: "))
print()
ExponentTotal = baseValue ** exponent
print()
print(baseValue, "raised to the power of", exponent, "is", ExponentTotal, "!!")
print()
print()
print("-----Addition and Subtraction-----")
print()
print()
StartInteger = int(input("Enter a starting integer: "))
AddInteger = int(input("Enter an integer to add: "))
SubtractInteger = int(input("Enter an integer to subtract: "))
print()
AddSubtractTotal = StartInteger + AddInteger - SubtractInteger
print()
print(StartInteger, "+", AddInteger, "-", SubtractInteger, "is equal to", AddSubtractTotal)
