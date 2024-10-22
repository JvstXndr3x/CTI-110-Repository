# Andrea Mejias
# 10/8/2024
# P2HW2
# Store a list of grades determining the features from each grade

module_list = [
    float(input("Enter grade for Module 1: ")),
    float(input("Enter grade for Module 2: ")),
    float(input("Enter grade for Module 3: ")),
    float(input("Enter grade for Module 4: ")),
    float(input("Enter grade for Module 5: ")),
    float(input("Enter grade for Module 9: ")),
]

average = sum(module_list) / 6

print()
print("------------Results------------")
print(f"{'Lowest Grade:':20} {min(module_list)}")
print(f"{'Highest Grade:':20} {max(module_list)}")
print(f"{'Sum of Grades:':20} {sum(module_list)}")
print(f"{'Average:':20} {average:<20.2f}")
print("---------------------------------------")
