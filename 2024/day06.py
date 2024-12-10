with open("2024/input06.txt") as f:
    grid = [list(x) for x in f.read().split()]

rows, cols = len(grid), len(grid[0])
visited = set()

# Up, Right, Down, Left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_idx = 0

initial_guard_position = next((
    (y, x) for y in range(rows)
    for x in range(cols) if grid[y][x] == "^"))

cy, cx = initial_guard_position
while True:
    visited.add((cy, cx))
    dy, dx = directions[dir_idx]
    ny, nx = cy + dy, cx + dx

    if not (0 <= ny < rows and 0 <= nx < cols):
        break

    if (grid[ny][nx] == "#"):
        dir_idx = (dir_idx + 1) % len(directions)
    else:
        cy, cx = ny, nx

print("Part 1:", len(visited))


def detect_loop(obstacle_position):
    cy, cx = initial_guard_position
    seen = set()
    d_idx = 0
    while True:
        state = (cy, cx, d_idx)
        if state in seen:
            return True
        seen.add((cy, cx, d_idx))

        dy, dx = directions[d_idx]
        ny, nx = cy + dy, cx + dx

        if not (0 <= ny < rows and 0 <= nx < cols):
            return False

        if (grid[ny][nx] == "#" or (ny, nx) == obstacle_position):
            d_idx = (d_idx + 1) % len(directions)
        else:
            cy, cx = ny, nx


print("Part 2:", sum(map(detect_loop, visited)))
