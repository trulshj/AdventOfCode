with open("2025/input04.txt") as f:
    grid = [list(x.rstrip()) for x in f.readlines()]

DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def step(grid):
    removed = 0
    new_grid = [row[:] for row in grid]

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '@':
                continue

            adjacent = sum(
                grid[ny][nx] == '@'
                for dy, dx in DELTAS
                if 0 <= (ny := y+dy) < len(grid) and 0 <= (nx := x+dx) < len(grid[0])
            )

            if adjacent < 4:
                removed += 1
                new_grid[y][x] = '.'

    return new_grid, removed


grid, removed = step(grid)
print("Part 1:", removed)


total_removed = removed

while True:
    grid, removed = step(grid)
    if removed == 0:
        break
    total_removed += removed

print("Part 2:", total_removed)
