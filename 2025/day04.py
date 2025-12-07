import grid_util as gu
from time_util import start_timer

timer = start_timer()


def step(grid: gu.Grid):
    to_remove = []

    def is_roll(cell): return cell == '@'

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if not is_roll(cell):
                continue

            adjacent = grid.count_neighbours(y, x, filter=is_roll)
            if adjacent < 4:
                to_remove.append((y, x))

    return to_remove


grid = gu.input_grid()

first = True
total_removed = 0

while True:
    to_remove = step(grid)
    if not to_remove:
        break

    if first:
        first = False
        print("Part 1:", len(to_remove))

    grid.bulk_set(to_remove, '.')
    total_removed += len(to_remove)

print("Part 2:", total_removed)
timer.stop().print()
