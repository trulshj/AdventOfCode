import re


def read_input():
    with open("input03.txt") as f:
        return f.read().rstrip()


def calculate_mul(mul: str):
    l, r = mul[4:-1].split(',')
    return int(l) * int(r)


memory = read_input()

muls = re.findall(r"mul\(\d+,\d+\)", memory)
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
