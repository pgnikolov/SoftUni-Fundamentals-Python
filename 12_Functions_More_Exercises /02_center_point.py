# You will be given the coordinates of two points on Cartesian coordinate system - X1, Y1, X2, Y2 on separate lines.
# Write function that prints point which is closest to the center of coordinate system (0, 0) in format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lower integer.
import math


def closest_point(x1, y1, x2, y2):
    if x1 ** 2 + y1 **2 <= x2 ** 2 + y2 ** 2:           # math.sqrt deosn't work with negative numbers give Value Error
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(closest_point(x1, y1, x2, y2))
