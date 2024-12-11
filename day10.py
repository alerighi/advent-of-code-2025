#!/usr/bin/env python3

import sys

from functools import cache

input = sys.stdin.read().splitlines()


@cache
def explore(y, x, s):
    if y < 0 or x < 0:
        return set(), 0

    try:
        v = int(input[y][x])
    except IndexError:
        return set(), 0
    except ValueError:
        return set(), 0

    if v != s + 1:
        return set(), 0  # invalid move

    if v == 9:
        return {(y, x)}, 1

    r_s = set()
    r_i = 0
    for (y, x) in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):
        s, i = explore(y, x, v)
        r_s |= s
        r_i += i

    return r_s, r_i


part_1 = 0
part_2 = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        s, i = explore(y, x, -1)
        part_1 += len(s)
        part_2 += i

print(f"PART 1: {part_1}")
print(f"PART 2: {part_2}")
