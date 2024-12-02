#!/usr/bin/env python3

reports = []

try:
    while True:
        reports.append(list(map(int, input().split())))
except EOFError:
    pass

def is_safe(report):
    old_d = 0
    for i in range(1, len(report)):
        d = report[i] - report[i-1]
        if abs(d) < 1 or abs(d) > 3 or old_d * d < 0:
            return False
        old_d = d

    return True

part_1 = 0
part_2 = 0
for report in reports:
    if is_safe(report):
        part_1 += 1 
        part_2 += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[(i+1):]):
                part_2 += 1
                break

print(f"PART 1: {part_1}")
print(f"PART 2: {part_2}")
