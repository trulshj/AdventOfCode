from collections import defaultdict
from itertools import combinations, count
from operator import add, sub

antennas = defaultdict(list)
with open("2024/input08.txt") as f:
    grid = f.read().split()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                antennas[cell].append((y, x))


def calculate_antenodes(a: tuple[int, int], b: tuple[int, int], n: int):
    dy, dx = b[0] - a[0], b[1] - a[1]
    for (y, x) in [a, b]:
        for op in [add, sub]:
            new_point = (op(y, dy * n), op(x, dx * n))
            if n == 0 or (new_point != a and new_point != b):
                yield new_point


def in_bounds(y: int, x: int):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def calculate_harmonics(only_first=False):
    antenodes = set()
    for group in antennas.values():
        for a, b in combinations(group, 2):
            harmonic_range = [1] if only_first else count()
            for n in harmonic_range:
                valid_nodes = {node for node in
                               calculate_antenodes(a, b, n) if in_bounds(*node)}

                if not valid_nodes:
                    break
                antenodes.update(valid_nodes)
    return len(antenodes)


print("Part 1:", calculate_harmonics(only_first=True))
print("Part 2:", calculate_harmonics())
