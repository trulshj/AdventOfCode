def count_xmases(grid):
    XMAS = ["XMAS", "SAMX"]
    ROWS = len(grid)
    COLS = len(grid[0])

    xmases = 0
    for y in range(ROWS):
        for x in range(COLS):

            if x + 3 < COLS:
                horizontal = grid[y][x:x+4]
                if horizontal in XMAS:
                    xmases += 1

            if y + 3 < ROWS:
                vertical = "".join(grid[y+i][x] for i in range(4))
                if vertical in XMAS:
                    xmases += 1

            if y + 3 < ROWS and x + 3 < COLS:
                ltr = "".join(grid[y+i][x+i] for i in range(4))
                if ltr in XMAS:
                    xmases += 1

            if y + 3 < ROWS and x - 3 >= 0:
                rtl = "".join(grid[y+i][x-i] for i in range(4))
                if rtl in XMAS:
                    xmases += 1

    return xmases


def count_x_mases(grid):
    x_mases = 0

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            if grid[y][x] != "A":
                continue

            corners = \
                grid[y-1][x-1] + \
                grid[y-1][x+1] + \
                grid[y+1][x+1] + \
                grid[y+1][x-1]

            if corners in ["MMSS", "SMMS", "SSMM", "MSSM"]:
                x_mases += 1

    return x_mases


with open("2024/input04.txt") as f:
    grid = f.read().split()

print("Part 1:", count_xmases(grid))
print("Part 2:", count_x_mases(grid))
