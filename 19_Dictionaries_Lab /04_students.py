# You will be receiving names of students, their ID, and a course of programming they have taken
# in the format "{name}:{ID}:{course}". On last line, you will receive name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course
# in the format: "{name} - {ID}" on separate lines.

command = input()
students = dict()

while ":" in command:
    info = command.split(":")
    name = info[0]
    id_std = info[1]
    course = info[2]
    if course not in students:
        students[course] = dict()
    students[course][name] = id_std

    command = input()

sort_course = " ".join(command.split("_"))

for k, v in students.items():
    if k == sort_course:
        for name, id_std in v.items():
            print(f"{name} - {id_std}")
