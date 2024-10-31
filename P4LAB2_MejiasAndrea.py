# Andrea Mejias
# 10/31/2024
# P4LAB2
# Program asks for multiplication table to be displayed

# While loop to control program running continuously
runagain = "y"

while runagain == "y" or runagain == "yes":
    userint = int(input("Enter an integer: "))
    if userint >=0:
        # Print the multiplication table.
        for num in range(1,13):
            print(f"{userint} * {num} = {userint * num}")
        
    else:
        print("Cannot accept negative values!)")
    runagain = input("Would you like to run the program again?").lower()
    validinputs = ["yes", "y", "no", "n",]
    # Validate the user's input
    while runagain not in validinputs:
        print("Invalid response entered!")
        runagain = input("Would you like to run the program again?").lower()

# Loop break.
print("Exiting program...")
