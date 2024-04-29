# You will receive some lines of input in the format "{contest}:{password for contest}" until you receive
# "end of contests". Save that data because you will need it later. After that you will receive another type of
# input in the format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".
# Here is what you need to do.
#     • Check if the contest is valid (It is considered valid if you received it in the first type of input)
#     • Check if the password is correct for the given contest
#     • If the contest and the password are valid, save the user with the contest they take part in
#     (a user can take part in many contests) and the points the user has in the given contest.
# If you receive the same contest and the same user update the points only if the new ones are more than the older ones.

contests = {}
participants = {}
best_score = {}
info = input()

while not info == "end of contests":
    info_contest = info.split(":")
    title = info_contest[0]
    password = info_contest[1]
    contests[title] = password
    info = input()

info_part = input()

while not info_part == "end of submissions":
    all_info = info_part.split("=>")
    contest = all_info[0]
    key = all_info[1]
    name = all_info[2]
    points = int(all_info[3])
    if contest in contests and key in contests[contest]:
        if name not in participants:
            participants[name] = {}
            best_score[name] = 0
        if contest not in participants[name]:
            participants[name].setdefault(contest, points)
            best_score[name] += points
        else:
            if points > participants[name][contest]:
                participants[name][contest] = points
                best_score[name] += points - participants[name][contest]

    info_part = input()

for candidate, result in best_score.items():
    if result == max(best_score.values()):
        print(f"Best candidate is {candidate} with total {int(result)} points.")

participants_sort = dict(sorted(participants.items()))

print("Ranking:")

for key, value in participants_sort.items():
    print(f"{key}")
    sort_values = sorted(value.items(), key=lambda x: x[1], reverse=True)
    for nkey, nvalue in sort_values:
        print(f"#  {nkey} -> {nvalue}")
