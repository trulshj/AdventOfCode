import utils.grid as g
from utils.time import start_timer
from functools import cache

timer = start_timer()

grid = g.input_grid()

start = next(grid.coords_with_value('S'))
splitters = set(grid.coords_with_value('^'))
hit_splitters = set()

queue = [start]
splits = 0
while queue:
    y, x = queue.pop()
    if y == grid.height:
        continue
    next_cell = (y+1, x)
    if next_cell in splitters:
        if next_cell in hit_splitters:
            continue
        splits += 1
        hit_splitters.add(next_cell)
        queue.append((y+1, x-1))
        queue.append((y+1, x+1))
    else:
        queue.append(next_cell)

print("Part 1:", splits)


@cache
def count(start: tuple[int, int]) -> int:
    if start[0] >= grid.height:
        return 1

    nxt = g.down(start)

    if nxt in splitters:
        return count(g.left(nxt)) + count(g.right(nxt))

    return count(nxt)


print("Part 2:", count(start))
timer.stop().print()
