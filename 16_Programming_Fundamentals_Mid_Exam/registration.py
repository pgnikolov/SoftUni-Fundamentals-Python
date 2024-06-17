username = input().strip()

while True:
    command = input().strip()

    if command == "Registration":
        break

    parts = command.split()
    cmd = parts[0]

    if cmd == "Letters":
        case = parts[1]
        if case == "Lower":
            username = username.lower()
        elif case == "Upper":
            username = username.upper()
        print(username)

    elif cmd == "Reverse":
        start_index = int(parts[1])
        end_index = int(parts[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            reversed_substring = substring[::-1]
            print(reversed_substring)

    elif cmd == "Substring":
        substring = parts[1]
        if substring in username:
            username = username.replace(substring, '', 1)
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif cmd == "Replace":
        char = parts[1]
        username = username.replace(char, '-')
        print(username)

    elif cmd == "IsValid":
        char = parts[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    else:
        print("Invalid command")


# username = input().strip()
#
# while True:
#     command = input().strip()
#
#     if command == "Registration":
#         break
#
#     parts = command.split()
#     cmd = parts[0]
#
#     if cmd == "Letters":
#         case = parts[1]
#         if case == "Lower":
#             username = username.lower()
#         elif case == "Upper":
#             username = username.upper()
#         print(username)
#
#     elif cmd == "Reverse":
#         start_index = int(parts[1])
#         end_index = int(parts[2])
#         if 0 <= start_index < len(username) and 0 <= end_index < len(username):
#             substring = username[start_index:end_index + 1]
#             reversed_substring = substring[::-1]
#             print(reversed_substring)
#
#     elif cmd == "Substring":
#         substring = parts[1]
#         if substring in username:
#             username = username.replace(substring, '', 1)
#             print(username)
#         else:
#             print(f"The username {username} doesn't contain {substring}.")
#
#     elif cmd == "Replace":
#         char = parts[1]
#         username = username.replace(char, '-')
#         print(username)
#
#     elif cmd == "IsValid":
#         char = parts[1]
#         if char in username:
#             print("Valid username.")
#         else:
#             print(f"{char} must be contained in your username.")
#
#     else:
#         print("Invalid command")
