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
participants = {}

command = input()

while not command == "no more time":
    info = command.split(" -> ")
    name = info[0]
    contest = info[1]
    points = int(info[2])
    if name not in participants:
        participants[name] = 0
    if contest not in contests:
        contests[contest] = {}
    if name not in contests[contest]:
        contests[contest][name] = points
        participants[name] += points
    else:
        if contests[contest][name] < points:
            participants[name] += points - contests[contest][name]
            contests[contest][name] = points

    command = input()

sorted_contests = {}
for key, value in contests.items():
    sorted_part = sorted(value.items(), key=lambda x: (-x[1], x[0]))
    sorted_contests[key] = dict(sorted_part)


for key, value in sorted_contests.items():
    print(f"{key}: {len(value)} participants")
    place = 0
    for nkey, nvalue in value.items():
        place += 1
        print(f"{place}. {nkey} <::> {nvalue}")

print("Individual standings:")
sorted_part = dict(sorted(participants.items(), key=lambda x: (-x[1])))
place = 0
for part, score in sorted_part.items():
    place += 1
    print(f"{place}. {part} -> {score}")

