# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

lines = int(input())
courses = list()

for _ in range(lines):
    course = input()
    courses.append(course)

print(courses)
