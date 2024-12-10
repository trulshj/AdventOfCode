with open("2024/input10.txt") as f:
    topo = [list(map(int, x)) for x in f.read().split()]


ORTHO = [(-1, 0), (1, 0), (0, -1), (0, 1)]

trailheads = [(y, x) for y in range(len(topo))
              for x in range(len(topo[0])) if topo[y][x] == 0]


def get_topo(y, x):
    if not (0 <= y < len(topo) and 0 <= x < len(topo[0])):
        return -1
    return topo[y][x]


def explore_trailhead(trailhead, mark_visited=True):
    queue = [(trailhead, 0)]
    visited = set()
    score = 0
    while queue:

        (cy, cx), height = queue.pop()
        if (cy, cx) in visited:
            continue
        elif mark_visited:
            visited.add((cy, cx))

        if height == 9:
            score += 1
            continue

        for dy, dx in ORTHO:
            ny, nx = cy + dy, cx + dx
            n_height = get_topo(ny, nx)
            if n_height == height + 1:
                queue.append(((ny, nx), n_height))
    return score


print("Part 1:",
      sum(map(explore_trailhead, trailheads)))
print("Part 2:",
      sum(map(lambda t: explore_trailhead(t, False), trailheads)))
