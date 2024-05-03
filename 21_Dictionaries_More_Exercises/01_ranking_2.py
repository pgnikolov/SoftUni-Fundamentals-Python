ranking_dict = {}
course_password_dict = {}
contest_dict = {}

while True:
    command_one = input().split(":")
    if command_one[0] == "end of contests":
        break
    key = command_one[0]
    password = command_one[1]
    course_password_dict[key] = password

while True:
    command_two = input().split("=>")
    if command_two[0] == "end of submissions":
        break
    contest = command_two[0]
    password = command_two[1]
    name = command_two[2]
    points = int(command_two[3])
    if contest in course_password_dict.keys():
        if course_password_dict[contest] == password:
            if name not in contest_dict.keys():
                contest_dict[name] = {}

            if contest in contest_dict[name].keys():
                if points > contest_dict[name][contest]:
                    contest_dict[name][contest] = points
            else:
                contest_dict[name][contest] = points

for key in contest_dict:
    ranking_dict[key] = sum(contest_dict[key].values())

max_score = (max(ranking_dict, key=ranking_dict.get))

print(f"Best candidate is {max_score} with total {ranking_dict[max_score]} points.")
print("Ranking:")

alphabetic_order_dict = sorted(contest_dict)

for part in alphabetic_order_dict:
    print(part)
    sorted_score = sorted(contest_dict[part], key=contest_dict[part].get, reverse=True)
    for course in sorted_score:
        print(f"#  {course} -> {contest_dict[part][course]}")
