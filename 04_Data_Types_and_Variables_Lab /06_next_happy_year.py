# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
#
# year = int(input())
#
# while True:
#     year += 1
#     seen = set()
#     for digit in str(year):
#         if digit in seen:
#             break
#         seen.add(digit)
#     else:
#         print(year)
#         break


def is_happy_year(year):
    return len(set(str(year))) == len(str(year))


def next_happy_year(year):
    while True:
        year += 1
        if is_happy_year(year):
            return year


year = int(input("Enter a year: "))
print("Next happy year:", next_happy_year(year))
