# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
# For each course, print the registered users.
#     • Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
#     • The product data is always delimited by " : "
# Output
#     • Print the information about each course in the following format:
# "{course_name}: {registered_students}"
#     • Print the information about each student in the following format:
# "-- {student_name}"

courses_info = {}

command = input()

while command != 'end':
    info = command.split(" : ")
    name = info[1]
    course = info[0]
    if course not in courses_info:
        courses_info[course] = []
    courses_info[course].append(name)
    command = input()

for course, names in courses_info.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")
