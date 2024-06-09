# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which
# is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous
# problem. If the lines are of equal length, print only the first one.
# The resulting coordinates must be formatted to the lower integer.
import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    lenght_line_one = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    lenght_line_two = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    if lenght_line_one > lenght_line_two:
        if x1 ** 2 + y1 ** 2 <= x2 ** 2 + y2 ** 2:
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        else:
            return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    else:
        if x3 ** 2 + y3 ** 2 <= x4 ** 2 + y4 ** 2:
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        else:
            return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
g = float(input())
h = float(input())
print(longer_line(a, b, c, d, e, f, g, h))

import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def closer(x1, y1, x2, y2):
    return (x1 ** 2 + y1 ** 2) <= (x2 ** 2 + y2 ** 2)


def format_point(x, y):
    return f"({math.floor(x)}, {math.floor(y)})"


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length_first = distance(x1, y1, x2, y2)
    length_second = distance(x3, y3, x4, y4)

    if length_first >= length_second:
        if closer(x1, y1, x2, y2):
            return format_point(x1, y1) + format_point(x2, y2)
        else:
            return format_point(x2, y2) + format_point(x1, y1)
    else:
        if closer(x3, y3, x4, y4):
            return format_point(x3, y3) + format_point(x4, y4)
        else:
            return format_point(x4, y4) + format_point(x3, y3)


# Read input
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
g = float(input())
h = float(input())

# Print the result
print(longer_line(a, b, c, d, e, f, g, h))