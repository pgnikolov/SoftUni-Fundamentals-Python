def make_upper(password, indx):
    password = password[:indx] + password[indx].upper() + password[indx+1:]
    return password


def make_lower(password, indx):
    password = password[:indx] + password[indx].lower() + password[indx+1:]
    return password


def insert_char(password, indx, char):
    password = password[:indx] + char + password[indx:]
    return password


def replace_char(password, char, value):
    if char in password:
        old_ascii = ord(char)
        new_ascii = old_ascii + int(value)
        new_char = chr(new_ascii)
        password = password.replace(char, new_char)
        return password


def validation(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    if not all(char.isalnum() or char == '_' for char in password):
        print("Password must consist only of letters, digits and _!")
    if not any(char.isupper() for char in password):
        print("Password must consist at least one uppercase letter!")
    if not any(char.islower() for char in password):
        print("Password must consist at least one lowercase letter!")
    if not any(char.isdigit() for char in password):
        print("Password must consist at least one digit!")


passw = input()

while True:
    command = input()
    if command == "Complete":
        break
    if command == "Validation":
        validation(passw)

    action = command.split()

    if action[0] == "Make" and action[1] == "Upper":
        passw = make_upper(passw, int(action[2]))
        print(passw)
    elif action[0] == "Make" and action[1] == "Lower":
        passw = make_lower(passw, int(action[2]))
        print(passw)
    elif action[0] == "Insert":
        passw = insert_char(passw, int(action[1]), action[2])
        print(passw)
    elif action[0] == "Replace":
        passw = replace_char(passw, action[1], action[2])
        print(passw)
    else:
        continue
