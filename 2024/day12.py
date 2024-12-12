
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
        garden_plots.append(plot)


def calculate_cost(garden_plot: set[tuple[int, int]]):
    area = len(garden_plot)

    perimeter = sum(
        4 - sum((y + dy, x + dx) in garden_plot for dy, dx in ORTHO)
        for y, x in garden_plot
    )

    sides = sum(
        (v not in garden_plot and h not in garden_plot) +  # Outer Corner
        (v in garden_plot and h in garden_plot and d not in garden_plot)  # Inner Corner
        for y, x in garden_plot
        for dy, dx in DIAGONAL
        for v, h, d in [((y + dy, x), (y, x + dx), (y + dy, x + dx))]
    )

    return area, perimeter, sides


p1 = p2 = 0
for plot in garden_plots:
    area, perimeter, sides = calculate_cost(plot)
    p1 += area * perimeter
    p2 += area * sides

print("Part 1:", p1)
print("Part 2:", p2)
