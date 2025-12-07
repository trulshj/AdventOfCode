from itertools import groupby
import utils.aoc as aoc
from math import prod


l = [x.split() for x in reversed(aoc.lines())]
problems = list(zip(*[l[0]] + [list(map(int, x)) for x in l[1:]]))
print("Part 1:", sum(prod(p[1:]) if p[0] ==
      '*' else sum(p[1:]) for p in problems))


def is_blank(p):
    return all(c == ' ' for c in p)


groups = groupby(list(zip(*[x.rstrip('\n')
                 for x in aoc.readlines()])), key=is_blank)
total = 0
for blank, block in groups:
    if blank:
        continue

    block = list(block)
    nums = [int("".join(col[:-1])) for col in block]
    if block[0][-1] == '*':
        total += prod(nums)
    else:
        total += sum(nums)

print("Part 2:", total)
