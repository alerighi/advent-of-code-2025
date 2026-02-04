#!/usr/bin/env python3

import sys

wires = {}
operations = []

for line in sys.stdin.readlines():
    line = line.strip()
    if ":" in line:
        wire, value = line.split(":")
        wires[wire] = value.strip() == "1"

    elif "->" in line:
        exp, result = line.split("->")
        left, op, right = exp.split()
        wires[result.strip()] = (left, op, right)

operators = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: a ^ b,
}


def get_wire(x):
    value = wires[x]
    if isinstance(value, bool):
        return value
    left, op, right = value
    wires[x] = operators[op](get_wire(left), get_wire(right))

    return wires[x]


z_keys = sorted(filter(lambda x: x.startswith("z"),
                wires.keys()), reverse=True)
part_1 = 0
for key in z_keys:
    value = get_wire(key)
    part_1 <<= 1
    part_1 |= value

print(f"PART 1: {part_1}")
