# Student Grade Calculator

# 1. Create a list of test scores for a student.
student_scores = (76, 81, 80)
maths, english, science = student_scores
print("Maths:", maths)
print("English:", english)
print("Science:", science)

# 2. Use floor division to calculate the average score.
average_score = sum(student_scores) // 3
print("Average Score:", average_score)

# 3. Use comparison operators to determine the grade based on the average score.
grade_astar = (90 <= average_score <= 100)
grade_a = (80 <= average_score < 90)
grade_b = (70 <= average_score < 80)
grade_c = (60 <= average_score < 70)
grade_d = (50 <= average_score < 60)
grade_e = (40 <= average_score < 50)
grade_f = (30 <= average_score < 40)
grade_g = (20 <= average_score < 30)
no_grade = (average_score < 20)

# 4. Use assignment operators to update the student's grade.
student_grade = ""
if grade_astar == True:
    student_grade += "A*"
elif grade_a == True:
    student_grade += "A"
elif grade_b == True:
    student_grade += "B"
elif grade_c == True:
    student_grade += "C"
elif grade_d == True:
    student_grade += "D"
elif grade_e == True:
    student_grade += "E"
elif grade_f == True:
    student_grade += "F"
elif grade_g == True:
    student_grade += "G"
else:
    student_grade += "No grade"
print("Overall Grade:", student_grade, "\n")

# 5. Use membership operators to check if a specific score exists in the list of scores.
score = int(93)
print("Score to check:", score)
if score in student_scores:
    print("This score is in the list of student scores.")
if score not in student_scores:
    print("This score is not in the list of student scores.")

# 6. Use identity operators to compare objects.
if (maths or english or science) is average_score:
    print("One of the scores is equivalent to the average score.")
if (maths or english or science) is not average_score:
    print("None of the scores are equivalent to the average score.")

# 7. Use bitwise operators to perform bitwise operations on the scores.
bitwise_operation = maths & english
print("Bitwise operation:", bitwise_operation)