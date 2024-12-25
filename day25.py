#!/usr/bin/env python3

import sys

input = sys.stdin.read().splitlines()
keys = []
locks = []

for i in range(0, len(input), 8):
    heights = [-1] * 5
    for j in range(5):
        for k in range(7):
            if input[i + k][j] == '#':
                heights[j] += 1

    if input[i][0] == '#':
        locks.append(heights)
    else:
        keys.append(heights)

part_1 = 0
for lock in locks:
    for key in keys:
        for l, k in zip(lock, key):
            if l + k > 5:
                break
        else:
            part_1 += 1

print(f"PART 1: {part_1}")
