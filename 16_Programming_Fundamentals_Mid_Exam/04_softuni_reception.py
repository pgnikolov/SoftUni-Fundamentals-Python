# Three employees are working in reception all day. Each of them can handle a different number of students per hour.
# Your task is to calculate how much time it will take to answer all the questions of a given number of students.
# First, you will receive 3 lines with integers, representing the number of students each employee can help per hour.
# On the following line, you will receive students count as a single integer.
# Every fourth hour, all employees have a break, so they don't work for an hour.
# It is the only break for the employees, because they don't need rest, nor have a personal life.
# Calculate time needed to answer all student's questions and print it in the following format:"Time needed: {time}h."
import math
emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())
students = int(input())
work_per_hour = emp_1 + emp_2 + emp_3
hours_work_needed = math.ceil(students / work_per_hour)
time_for_breaks = hours_work_needed // 3

if hours_work_needed % 3 == 0 and not hours_work_needed == 0:
    time_for_breaks -= 1

print(f"Time needed: {hours_work_needed + time_for_breaks}h.")

