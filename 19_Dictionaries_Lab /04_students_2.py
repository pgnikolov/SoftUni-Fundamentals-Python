students_dict = {}
course = ""

while True:
    info = input().split(":")
    if info[0][0].isupper():
        students_dict[info[1]] = info[0], info[2]
    else:
        course = ' '.join(info[0].split("_"))
        break

for k in students_dict:
    if students_dict[k][1] == course:
        print(f"{students_dict[k][0]} - {k}")
        