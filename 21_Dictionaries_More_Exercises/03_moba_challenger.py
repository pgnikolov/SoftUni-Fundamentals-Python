# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number.
# You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present,
# else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
#     • If they have at least one position in common, the player with better total skill points wins
#     and the other is demoted from the tier -> remove him.
#     • If they have the same total skill points at the same positions,
#     the duel is tied and they both continue in the Season.
#     • If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players,
# ordered by total skill in descending order, then ordered by player name in ascending order.
# For each player print their position and skill, ordered descending by skill,
# then ordered by position name in ascending order.

players_stats = {}
total_skills = {}

command = input()

while not command == "Season end":
    if "->" in command:
        info = command.split(" -> ")
        player = info[0]
        position = info[1]
        skill = int(info[2])
        if player not in players_stats:
            total_skills[player] = skill
            players_stats[player] = {}
            players_stats[player][position] = skill
        elif position not in players_stats[player]:
            players_stats[player][position] = skill
            total_skills[player] += skill
        else:
            if skill > players_stats[player][position]:
                players_stats[player][position] = skill
                total_skills += skill - players_stats[player][position]
    elif "vs" in command:
        players_duel = command.split(" vs ")
        player1 = players_duel[0]
        player2 = players_duel[1]
        if not (player1 in players_stats and player2 in players_stats):
            command = input()
            continue
        for positions in players_stats[player1]:
            if positions not in players_stats[player2]:
                continue
            else:
                if total_skills[player1] > total_skills[player2]:
                    players_stats.pop(player2)
                    total_skills.pop(player2)
                    break
                elif total_skills[player2] > total_skills[player1]:
                    players_stats.pop(player1)
                    total_skills.pop(player1)
                    break
    command = input()

for key, value in sorted(total_skills.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value} skill")
    for nkey, nvalue in sorted(players_stats[key].items(), key=lambda x: (-x[1], x[0])):

        print(f"- {nkey} <::> {nvalue}")
