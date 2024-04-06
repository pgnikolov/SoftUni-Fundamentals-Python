# Your task is to define how much coffee you need to stay awake. Until you receive the command "END",
# you need to read commands on different lines.
# alculate the number of coffees you need to drink to stay awake
# list of events - 'coding', 'dog', 'cat', 'movie'
# f other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
# • If it is lowercase, you need 1 coffee by an event.
# • If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".
not_end = True
coffe_counter = 0

while not_end:
    event = input()
    if event.lower() == 'coding' or event.lower() == 'dog' or event.lower() == 'cat' or event.lower() == 'movie':
        if event == event.lower():
            coffe_counter += 1
        elif event == event.upper():
            coffe_counter += 2
        else:
            pass
    elif event == "END":
        not_end = False
        if coffe_counter > 5:
            print("You need extra sleep")
        else:
            print(coffe_counter)
    else:
        pass
