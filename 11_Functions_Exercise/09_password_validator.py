# Write a function that checks if a given password is valid. Password validations are:
#     • It should be 6 - 10 (inclusive) characters long
#     • It should consist only of letters and digits
#     • It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
#     • "Password must be between 6 and 10 characters"
#     • "Password must consist only of letters and digits"
#     • "Password must have at least 2 digits"

def is_valid_password(password):
    length_valid = 6 <= len(password) <= 10
    digits_valid = sum(c.isdigit() for c in password) >= 2
    alphanumeric_valid = all(c.isalnum() for c in password)
    error_msg = ""
    if length_valid and digits_valid and alphanumeric_valid:
        return "Password is valid"
    else:
        if not length_valid:
            error_msg = "Password must be between 6 and 10 characters"
        if not alphanumeric_valid:
            error_msg += "\nPassword must consist only of letters and digits"
        if not digits_valid:
            error_msg += "\nPassword must have at least 2 digits"
        return error_msg


password = input()
print(is_valid_password(password))
