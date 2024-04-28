# You will receive lines in the following format:"{username}-{language}-{points}" until you receive "exam finished".
# You should store each username and their submissions and points. If a student has two or more submissions
# for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned".
# In that case, you should remove the user from the contest but preserve his submissions in the total count
# of submissions for each language.
# After receiving the "exam finished", print each of the participants in the following format:

info = input()

results = {}
submissions = {}

while not info == "exam finished":
    split_info = info.split("-")
    student = split_info[0]
    command = split_info[1]
    points = 0
    if len(split_info) > 2:
        points = int(split_info[2])

    if not command == "banned":
        if student in results:
            if results[student] < points:
                results[student] = points
        else:
            results[student] = points
        if command not in submissions:
            submissions[command] = 0
        submissions[command] += 1

    else:
        results.pop(student)

    info = input()

print("Results:")
for student, points in results.items():
    print(f"{student} | {points}")

print("Submissions:")
for lang, count in submissions.items():
    print(f"{lang} - {count}")
