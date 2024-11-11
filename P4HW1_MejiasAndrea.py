# Andrea Mejias
# 11/10/2024
# P4HW1
# Store a list of grades determining the features from each grade by using loops

# Ask for how many loops will be iterated in the program
numScores = int(input("How many scores are you calculating? "))

# Store a list of all score inputs from each loop to be used for other list actions
InputScores = []

# Add a for loop for all score inputs ranging from 0-100
for score in range(numScores):
    userInput = int(input(f"Enter score # {score + 1}: "))
    # Add a while loop initiating an invalid statement if invalid values are entered
    while userInput < 0 or userInput > 100:
        print(f"Invalid score entered. Score should be between or equal to 0 and 100.")
        userInput = int(input(f"Enter score # {score + 1} again: "))
    # Add valid scores into the list using the append action
    InputScores.append(userInput)
    
# Print out results after the for and while loops are initiated
print()
print("------------Results------------")
print(f"{'Lowest Grade:':20} {min(InputScores)}")
# Remove lowest score from list before printing it
InputScores.remove(min(InputScores))
print()
# Print score after modified with the removal of the lowest score
print(f"-----Your Scores (Excluding the Lowest)-----")
print(InputScores)
print()
# Display average just like you did in P2HW2
average = sum(InputScores) / numScores
# Use If Else statements to determine and display which letter grade matches the average score
print(f"{'Average:':20} {average:<20.2f}")
if average >= 90:
    print(f"You have an A for all scores.")
elif average >= 80:
    print(f"You have a B for all scores.")
elif average >= 70:
    print(f"You have a C for all scores.")
elif average >= 60:
    print(f"You have a D for all scores.")
else:
    print(f"You have an F for all scores.")
print("---------------------------------------")
