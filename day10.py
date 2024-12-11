#!/usr/bin/env python3

from functools import cache

stones = list(map(int, input().split()))


@cache
def n_split(n, v):
    if n == 0:
        return 1

    if v == 0:
        return n_split(n - 1, 1)

    if len(v_str := str(v)) % 2 == 0:
        mid = len(v_str) // 2

        return n_split(n - 1, int(v_str[:mid])) + n_split(n - 1, int(v_str[mid:]))

    return n_split(n - 1, v * 2024)


print(f"PART 1: {sum(n_split(25, v) for v in stones)}")
print(f"PART 2: {sum(n_split(75, v) for v in stones)}")
