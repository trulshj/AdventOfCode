
area = [x.rstrip() for x in open("input-03.txt").readlines()]
slopes = [(1,), (3,), (5,), (7,), (1, 2)]


def check_slope(right, down=1, area=area):
    trees = 0
    current_col = 0
    width = len(area[0])

    for row in area[::down]:
        if row[current_col % width] == '#':
            trees += 1
        current_col += right
    return trees


tree_counts = [check_slope(*x) for x in slopes]
tree_product = 1
for count in tree_counts:
    tree_product *= count

print(f"Part 1: {tree_counts[1]}")
print(f"Part 2: {tree_product}")
