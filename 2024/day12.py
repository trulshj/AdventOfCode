
with open("2024/input12.txt") as f:
    grid = f.read().split()


def get_grid(y, x):
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
        return None
    return grid[y][x]


ORTHO = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIAGONAL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = set()
garden_plots = []


for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if (y, x) in visited:
            continue

        plot = set()
        stack = [(y, x)]
        while stack:
            c = stack.pop()
            if c in visited:
                continue
            plot.add(c)
            visited.add(c)

            for dy, dx in ORTHO:
                ny, nx = c[0]+dy, c[1]+dx
                if get_grid(ny, nx) == cell:
                    stack.append((ny, nx))
        garden_plots.append((cell, plot))


def calculate_cost(garden_plot: tuple[str, set[tuple[int, int]]]):
    coords = garden_plot[1]
    area = len(coords)

    perimeter = 0
    for y, x in coords:
        p = 4
        for dy, dx in ORTHO:
            p -= (y+dy, x+dx) in coords
        perimeter += p

    sides = 0
    for y, x in coords:
        for dy, dx in DIAGONAL:
            # Vertical, Horizontal, Diagonal
            v, h, d = (y+dy, x), (y, x+dx), (y+dy, x+dx)
            sides += v not in coords and h not in coords  # Outer Corner
            sides += v in coords and h in coords and d not in coords  # Inner Corner

    return area, perimeter, sides


p1 = 0
p2 = 0
for plot in garden_plots:
    area, perimeter, sides = calculate_cost(plot)
    p1 += area * perimeter
    p2 += area * sides

print("Part 1:", p1)
print("Part 2:", p2)
