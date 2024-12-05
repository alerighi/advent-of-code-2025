#!/usr/bin/env python3

import sys

input = sys.stdin.read().strip().splitlines()
Y = len(input)
X = len(input[0])

def get(y, x):
    if y >= 0 and y < Y and x >= 0 and x < X:
        return input[y][x]

    return ""

part_1 = 0
part_2 = 0
for y in range(Y):
    for x in range(X):
        for dy, dx in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            for i, c in enumerate("XMAS"):
                if c != get(y + dy * i, x + dx * i):
                    break
            else:
                part_1 += 1

        if input[y][x] == "A":
            d1 = get(y - 1, x - 1) + get(y + 1, x + 1)
            d2 = get(y - 1, x + 1) + get(y + 1, x - 1)

            if d1 in ("MS", "SM") and d2 in ("MS", "SM"):
                part_2 += 1

print(f"PART 1: {part_1}")
print(f"PART 2: {part_2}")