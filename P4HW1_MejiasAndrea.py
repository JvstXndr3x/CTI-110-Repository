# Andrea Mejias
# 11/10/2024
# P4HW1
# Store a list of grades determining the features from each grade by using loops

numScores = int(input("How many scores are you calculating? "))

InputScores = []

for score in range(numScores):
    userInput = int(input(f"Enter score # {score + 1}: "))
    while userInput < 0 or userInput > 100:
        print(f"Invalid score entered. Score should be between or equal to 0 and 100.")
        userInput = int(input(f"Enter score # {score + 1} again: "))
    InputScores.append(userInput)
    

print()
print("------------Results------------")
print(f"{'Lowest Grade:':20} {min(InputScores)}")
InputScores.remove(min(InputScores))
print()
print(f"-----Your Scores (Excluding the Lowest)-----")
print(InputScores)
print()
average = sum(InputScores) / numScores
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
