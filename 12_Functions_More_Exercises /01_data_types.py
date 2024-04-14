# Write a function that, depending on the first line of input, reads one of following string:"int","real", or"string".
#     • If the data type is an int, multiply the number by 2.
#     • If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
#     • If the data type is a string, surround the input with "$".
# Print the result on the console.

def data_type(first, second):
    if first == "int":
        return int(second) * 2
    elif first == "real":
        return f"{(float(second) * 1.5):.2f}"
    elif first == "string":
        return f"${second}$"


types = input()
datas = input()
print(data_type(types, datas))
