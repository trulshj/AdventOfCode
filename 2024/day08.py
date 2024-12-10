from collections import defaultdict
from itertools import combinations, count
from operator import add, sub

with open("2024/input08.txt") as f:
    grid = f.read().split()

antennas = defaultdict(list)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != '.':
            antennas[grid[y][x]].append((y, x))

antenodes = set()


def calc_antenodes(y1: int, x1: int, y2: int, x2: int, n=1):
    dy = y2 - y1
    dx = x2 - x1

    ans = set()

    for (y, x) in [(y1, x1), (y2, x2)]:
        for op in [add, sub]:
            ans.add((op(y, dy*n), op(x, dx*n)))

    return list(ans)


def in_bounds(y: int, x: int):
    return (0 <= y < len(grid) and 0 <= x < len(grid[0]))


for group in antennas.values():
    for a, b in combinations(group, 2):
        for an in calc_antenodes(*a, *b):
            if in_bounds(*an) and an != a and an != b:
                antenodes.add(an)


def get_antenodes():
    antenodes = set()
    for group in antennas.values():
        for a, b in combinations(group, 2):
            for i in count(1):
                ans = calc_antenodes(*a, *b, i)
                valid_nodes = list(
                    filter(lambda x: x[1], zip(ans, map(lambda x: in_bounds(*x), ans))))
                if len(valid_nodes) == 0:
                    break
                for n in valid_nodes:
                    antenodes.add(n)


def debug_antenodes():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in antenodes:
                print('#', end='')
            else:
                print(grid[y][x], end='')
        print()


print(len(antenodes))
print(len(antenodes2))
