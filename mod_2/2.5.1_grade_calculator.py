exam1_grade = float(input('Enter score on Exam 1 (out of 50):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 50):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50):\n'))

# overall_grade = (exam1_grade + exam2_grade + exam3_grade + exam4_grade) / 200

# score = overall_grade * 100

print('Your score is:', score )
print('Your overall grade is:', overall_grade)

######################################

exam1_grade = float(input('Enter score on Exam 1 (out of 50):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 50):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50):\n'))

overall_grade = (exam1_grade + exam2_grade + exam3_grade + exam4_grade) / 250

score = overall_grade * 100

print('Your score is:', score )
print('Your overall grade is:', overall_grade)

########################################################################
exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

prog_score_1 = float(input('Enter score on assignments 1 (out of 50):\n'))
prog_score_2 = float(input('Enter score on assignments 2 (out of 50):\n'))
prog_score_3 = float(input('Enter score on assignments 3 (out of 50):\n'))
prog_score_4 = float(input('Enter score on assignments 4 (out of 50):\n'))

average_exam_score = print((exam1_grade + exam2_grade + exam3_grade) / 300)

average_prog_score = print((prog_score_1 + prog_score_2 + prog_score_3 + prog_score_4) / 200)

overall_grade = print(( 0.6  * average_exam_score) + (0.4 * average_prog_score))

score = overall_grade + average_prog_score * 100

print('Your score is:', score )
print('Your overall grade is:', overall_grade)