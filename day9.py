#!/usr/bin/env python3

blocks = input()

fs = []
id = 0
files = []
free = []
for i, c in enumerate(map(int, blocks)):
    if i % 2 == 1:
        free.append(c)
        for _ in range(c):
            fs.append(-1)
    else:
        files.append(c)
        for _ in range(c):
            fs.append(id)
        id += 1

j = len(fs) - 1
for i in range(len(fs)):
    if fs[i] == -1:
        while fs[j] == -1:
            j -= 1
        if j <= i:
            break

        fs[i], fs[j] = fs[j], fs[i]


part_1 = 0
for i, b in enumerate(fs):
    if b == -1:
        break
    part_1 += i * b

print(f"PART 1: {part_1}")

assign = [-1 for i in range(len(free))]
for id, f in reversed(list(enumerate(files))):
    print(files)
    print(assign)

    for i in range(id):
        if free[i] <= f and assign[i] == -1:
            assign[i] = id
            files[id] = -1
            break

print(files)
print(assign)
part_2 = 0
c = 0
for file, assign in zip(files, assign):
    if file != -1:
        for i in range(file):
            part_2 += file * c
            c += 1
    if assign != -1:
        for i in range(assign):
            part_2 += assign * c
            c += 1

print(f"PART 2: {part_2}")
