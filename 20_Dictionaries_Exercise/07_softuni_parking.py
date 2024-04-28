# SoftUni got a new fancy parking lot. It has online parking validation. It can only receive users' data,
# but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
#     • "register {username} {license_plate_number}":
#         ◦ The system only supports one car per user at the moment, so if a user tries to register another
#         license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
#         ◦ If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
#     • "unregister {username}":
#         ◦ If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
#         ◦ If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all the commands, print all currently registered users and their license plates in the format:
#     • "{username} => {license_plate_number}"
parking = {}

n = int(input())

for i in range(n):
    info = input().split(' ')
    command = info[0]
    name = info[1]
    if command == "register":
        plate = info[2]
        if name not in parking:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")
    elif command == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            del parking[name]
            print(f"{name} unregistered successfully")

for k, v in parking.items():
    print(f"{k} => {v}")
