# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

"""
Author: Emely Chuy
Date: 10/18/2024
"""

#The first statement that'll be printed, user will insert # information
exam_one = int(input("Input exam grade one: "))

#The second statement that'll be printed, user will insert # information
exam_two = int(input("Input exam grade two: "))

#The third statement that'll be printed, user will insert # information
exam_three = int(input("Input exam grade three: "))

#This is a variable
grades = [exam_one, exam_two, exam_three]

#Sum to zero
sum_of_grades = 0

#Loop through each grade
for grade in grades:
    #Grade will be added
  sum_of_grades = sum(grades)

#This will make the average of the exams user chooses
avg = sum_of_grades / len(grades)

#If else statement begins, starting with the letter A, ending with F
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 89:
    letter_grade = "B"
elif avg >= 70 and avg < 79:
    letter_grade = "C"
elif avg >= 60 and avg < 69:
    letter_grade = "D"
else:
    letter_grade = "F"

#Each grade will be printed
for grade in grades:
    print("Exam: " + str(grade))

#This will print the average
print("Average: " + str(avg))

#This will print the final grade for the user
print("Grade: " + letter_grade)

#This will print if student is failing
if letter_grade == "F":
    print("Student is failing.")
    #If they are not failing, this will print
else:
    print("Student is passing.")
