#!/usr/bin/env python3

import re
import sys

input = sys.stdin.read()

part_1 = 0
part_2 = 0
enabled = True
for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", input):
    if do:
        enabled = True
    elif dont:
        enabled = False
    else:
        mul = int(a) * int(b)
        part_1 += mul
        if enabled:
            part_2 += mul

print(f"PART 1: {part_1}")
print(f"PART 2: {part_2}")


