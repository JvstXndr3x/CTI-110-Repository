# Andrea Mejias
# 11/14/2024
# P5LAB
# Use functions to similuate self-checkout

import random

def calculateCashBack():
    # Generate a random float for the amount owed to the store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")
    cash = float(input("How much cash will you put in the self-checkout? "))
    # Calculate cash back
    cash_back = cash - total_owed
    return cash_back
    print()

def disperseCashBack(change):

    # Convert the float value into an integer
    change = int(change * 100)

    if change == 0:
        print("No change due.")
        return
    elif change != 0:
        cash_back = change
        print(f"Change is ${change / 100:.2f}")

    # Add if statements to calculate change from the total

    numberofdollars = change // 100
    if numberofdollars > 1:
        print(f"{numberofdollars} Dollars")
    elif numberofdollars == 1:
        print(f"{numberofdollars} Dollar")

    change = change - (numberofdollars * 100)

    numberofquarters = change // 25
    if numberofquarters > 1:
        print(f"{numberofquarters} Quarters")
    elif numberofquarters == 1:
        print(f"{numberofquarters} Quarter")

    change = change - (numberofquarters * 25)

    numberofdimes = change // 10
    if numberofdimes > 1:
        print(f"{numberofdimes} Dimes")
    elif numberofdimes == 1:
        print(f"{numberofdimes} Dime")

    change = change - (numberofdimes * 10)

    numberofnickels = change // 5
    if numberofnickels > 1:
        print(f"{numberofnickels} Nickels")
    elif numberofnickels == 1:
        print(f"{numberofnickels} Nickel")

    change = change - (numberofnickels * 5)

    numberofpennies = change
    if numberofpennies > 1:
        print(f"{numberofpennies} Pennies")
    elif numberofpennies == 1:
        print(f"{numberofpennies} Penny")
    

# Define the main
def main():
    print("*****Welcome to the self-checkout!*****")
    cash_back = calculateCashBack()
    disperseCashBack(cash_back)

# Call the main
if __name__ == "__main__":
    main()
