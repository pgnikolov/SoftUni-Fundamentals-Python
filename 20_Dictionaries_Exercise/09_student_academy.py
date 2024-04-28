# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

grades_dict = {}

n = int(input())

for i in range(n):
    name = input()
    grade = float(input())
    if name not in grades_dict:
        grades_dict[name] = []
    grades_dict[name].append(grade)

for name, grade in grades_dict.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f"{name} -> {(sum(grade) / len(grade)):.2f}")
        