# Create a program that calculates bonus points for each student enrolled in a course.
# On the first line, you are going to receive the number of students. On the second line, you will receive
# the total number of lectures in the course. The course has an additional bonus, which you will receive on the
# third line. On the following lines, you will be receiving the count of attendances for each student.
# The bonus is calculated with the following formula:
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# Find the student with the maximum bonus and print them, along with his attendance, in the following format:
# "Max Bonus: {max bonus points}."
# "The student has attended {student attendances} lectures."
# Round the bonus points at the end to the nearest larger number.

import math

students_amount = int(input())
lectures = int(input())
bonus = int(input())
max_attendance = 0

for student in range(students_amount):
    attendance = float(input())
    if attendance > max_attendance:
        max_attendance = attendance
    if lectures == 0:
        max_bonus_point = 0
    else:
        max_bonus_point = max_attendance / lectures * (5 + bonus)

print(f"Max Bonus: {math.ceil(max_bonus_point)}.")
print(f"The student has attended {max_attendance:.0f} lectures.")
