from functools import cmp_to_key
from math import prod


def compare(l, r):
    l = l if isinstance(l, list) else [l]
    r = r if isinstance(r, list) else [r]
    for l2, r2 in zip(l, r):
        if isinstance(l2, list) or isinstance(r2, list):
            rec = compare(l2, r2)
        else:
            rec = r2 - l2
        if rec != 0:
            return rec
    return len(r) - len(l)


data = open("../inputs/day13.txt").read().strip()
pairs = [list(map(eval, p.split("\n"))) for p in data.split("\n\n")]
packets = sorted([y for x in pairs for y in x] + [[[2]], [[6]]], key=cmp_to_key(compare), reverse=True)
print(f"Part 1: {sum(i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) > 0)}")
print(f"Part 2: {prod([n for n, packet in enumerate(packets, 1) if packet in ([[2]], [[6]])])}")
