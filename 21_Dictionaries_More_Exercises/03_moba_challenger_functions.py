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

def player_stats_dict(name, position, score, players_info_dict):
    if name not in players_info_dict:
        players_info_dict[name] = {}
    if position not in players_info_dict[name]:
        players_info_dict[name][position] = 0
    if score > players_info_dict[name][position]:
        players_info_dict[name][position] = score
    return players_info_dict


def battle(player1, player2, players_info_dict):
    if player1 in players_info_dict and player2 in players_info_dict:
        if players_info_dict[player1].items == players_info_dict[player2].items:
            # both players have the same positions and equal points
            pass
        else:
            same_positions = 0
            for position in (players_info_dict[player1].keys()):
                if position in players_info_dict[player2].keys():
                    same_positions += 1
            if same_positions > 0:          # Search for at least 1 pos in common
                first_player_total_score = sum(players_info_dict[player1].values())
                second_player_total_score = sum(players_info_dict[player2].values())
                if first_player_total_score > second_player_total_score:
                    players_info_dict.pop(player2)
                elif second_player_total_score > first_player_total_score:
                    players_info_dict.pop(player1)
            else:
                # players don't have position in common
                pass
    return players_info_dict


players_dict = {}

while True:
    new_input = input()
    if new_input == "Season end":
        break
    elif "->" in new_input:
        player, position, point = new_input.split(" -> ")
        players_dict = player_stats_dict(player, position, int(point), players_dict)
    else:
        player_one, player_two = new_input.split(" vs ")
        players_dict = battle(player_one, player_two, players_dict)

sorted_max_score_dict = {player: sum(players_dict[player].values()) for player in players_dict}

sorted_max_score_names = sorted(sorted_max_score_dict.items(), key=lambda k: (-k[1], k[0]))

for key, value in sorted_max_score_names:
    print(f"{key}: {value} skill")
    player_roles_final = sorted(players_dict[key].items(), key=lambda k: (-k[1], k[0]))
    for nkey, nvalue in player_roles_final:
        print(f"- {nkey} <::> {nvalue}")
