# You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
#     • If there is no such force user and no such force side -> create a new
#     force side and add the force user to correspond side.
#     • Only if there is no such force user in any force side -> add the force user to the corresponding side.
#     • If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
#     • If there is such force user already -> change their side.
#     • If there is no such force user in any force side -> add the force user to the corresponding force side.
#     • If there is no such force user and no such force side -> create new force side and add the
#     force user to the corresponding side.
#     • Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo".
# At that point, you should print each force side. For each side, print the force users.
# In case there are no forced users on a side, you shouldn't print the side information.
# Input / Constraints
#     • The input comes in the form of commands in one of the formats specified above.
#     • The input ends when you receive the command "Lumpawaroo".

command = input()

sides_dict = {}
all_users = []
while command != "Lumpawaroo":
    if "|" in command:
        info = command.split(" | ")
        fside = info[0]
        fuser = info[1]
        if fuser not in all_users:
            if fside not in sides_dict:
                sides_dict[fside] = []
                if fuser not in sides_dict[fside]:
                    sides_dict[fside].append(fuser)
                    all_users.append(fuser)
    if "->" in command:
        info = command.split(" -> ")
        fuser = info[0]
        fside = info[1]
        if fside not in sides_dict:
            sides_dict[fside] = []
        for side, users in sides_dict.items():
            if fuser in users:
                sides_dict[side].remove(fuser)
        sides_dict[fside].append(fuser)
        print(f"{fuser} joins the {fside} side!")
    command = input()

for side, users in sides_dict.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
