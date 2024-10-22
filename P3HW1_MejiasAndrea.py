# Andrea Mejias
# 10/22/2024
# P3HW1
# Debugging a program with comments and fixes
# The beginning comments is not written properly and was only typed with a placeholder comment and the user's last name.

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
# All list values are not in order and do not match the values listed in the group "grades."
# Some quotation marks do not match. Spacing is also a small issue seen in here.
# List values need to be defined as a float input as grades are similar to a float.

grades = [
   float(input('Enter grade for Module 1: ')),
   float(input('Enter grade for Module 2: ')),
   float(input('Enter grade for Module 3: ')),
   float(input('Enter grade for Module 1: ')),
   float(input('Enter grade for Module 5: ')),
   float(input('Enter grade for Module 6: ')),
]

# add grades entered to a list
# Names for values are case-sensitive and some values don't match.
# This type of listing is unnecessary as all inputs must be listed INSIDE the list repository.
# No string names are needed for list values.

# TO DO: determine lowest, highest , sum and average for grades
# The function to find the highest value out of a list is max and not high. The list name is case-sensitive too.
# The value "sum" for the sum of all values on the list is automatically considered a functioning value, so it needs to be changed.
# Format needs to have some arrangement. 

low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / 6

# determine letter grade for average
# No equation is written for determining the average of the list values.
# Average is determined by using the sum of all values on the list and dividing it by how many values are on the list.


if avg >= 90:
 print('Your grade is: A')
else:
 if avg > 80:
  print('Your grade is: B')
 else:
  if avg > 70:
   print('Your grade is: C')
  else:
   if avg > 60:
    print('Your grade is: D')
   else:
    print('Your grade is: F') # TO DO: Finish this

# Indents need to be present in python if statements.
# Values in the if statements do not match together.



