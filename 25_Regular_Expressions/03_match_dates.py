import re

main_string = input()

patterns = re.compile(r"(?P<Day>[0-9]{2})([\.\-/])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>[0-9]{4})\b")
result = re.finditer(patterns, main_string)

for show in result:
    print(f"Day: {show['Day']}, Month: {show['Month']}, Year: {show['Year']}")
