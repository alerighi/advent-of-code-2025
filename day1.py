#!/usr/bin/env python3

l1 = []
l2 = []

while True:
    try:
        i1, i2 = map(int, input().split())
        l1.append(i1)
        l2.append(i2)
    except EOFError: 
        break 

l1.sort()
l2.sort()

part_1 = 0
for a, b in zip(l1, l2):
    part_1 += abs(a - b)

print(f"PART 1: {part_1}")

freq = {}
for i in l2:
    freq[i] = freq.get(i, 0) + 1

part_2 = 0
for i in l1:
    part_2 += i * freq.get(i, 0)

print(f"PART 2: {part_2}")
