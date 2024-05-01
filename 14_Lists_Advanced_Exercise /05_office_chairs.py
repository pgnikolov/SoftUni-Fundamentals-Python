# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room
# and the number of visitors. Each chair will be presented with the char "X". Next, there will be a single
# space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
#     • If there are not enough chairs in a specific room, print the following message:
#     "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
#     • Otherwise, print: "Game On, {total_free_chairs} free chairs left".

num = int(input())

total_free_chairs = 0
more_visitors_room = 0

for i in range(1, num + 1):
    info = input().split(" ")
    chairs = len(info[0])
    visitors = int(info[1])
    if chairs > visitors:
        total_free_chairs += chairs - visitors
    elif visitors > chairs:
        more_visitors_room += 1
        print(f"{visitors-chairs} more chairs needed in room {i}")

if more_visitors_room == 0:
    print(f"Game On, {total_free_chairs} free chairs left")


