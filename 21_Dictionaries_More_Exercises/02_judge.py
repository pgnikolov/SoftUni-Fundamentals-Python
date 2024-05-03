# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number.
# You need to keep track of every contest and points of each user:
#     • If the user has already participated in the contest, update their points only
#     if the new ones are more than the older ones.
#     • Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time". At that point, you should print each
# contest in order of input, for each contest print the participants ordered by points in descending order,
# then ordered by name in ascending order. After that, you should print individual statistics for
# every participant ordered by total points in descending order, and then by alphabetical order.

contests = {}
part_dict = {}

command = input()

while not command == "no more time":
    info = command.split(" -> ")
    name = info[0]
    contest = info[1]
    points = int(info[2])
    if name not in part_dict:
        part_dict[name] = 0
    if contest not in contests:
        contests[contest] = {}
    if name not in contests[contest]:
        contests[contest][name] = points
        part_dict[name] += points
    else:
        if contests[contest][name] < points:
            part_dict[name] += points - contests[contest][name]
            contests[contest][name] = points

    command = input()

sorted_contests = {}
for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_part = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    place = 0
    for participant, score in sorted_part:
        place += 1
        print(f"{place}. {participant} <::> {score}")

print("Individual standings:")
sorted_part_dict = sorted(part_dict.items(), key=lambda x: (-x[1], x[0]))
place = 0
for part, score in sorted_part_dict:
    place += 1
    print(f"{place}. {part} -> {score}")

