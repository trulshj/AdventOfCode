import re
from math import prod

with open("input03.txt") as f:
    memory = f.read().rstrip()

muls = re.findall(r"mul\(\d+,\d+\)", memory)


def calculate_mul(x): return prod(map(int, x[4:-1].split(",")))


print("Part 1:", sum(map(calculate_mul, muls)))


instructions = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", memory)

total = 0
enabled = True
for instruction in instructions:
    match instruction:
        case ('', do, ''):
            enabled = True
        case ('', '', dont):
            enabled = False
        case (mul, '', ''):
            if enabled:
                total += calculate_mul(mul)

print("Part 2:", total)
