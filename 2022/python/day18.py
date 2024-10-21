from utils import print_day

DAY = 18


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return [tuple(map(int, x.rstrip().split(","))) for x in f.readlines()]


def part1(data):
    cubes = set(data)
    neighbours = [
        (0,  0,  1),
        (0,  0, -1),
        (0,  1,  0),
        (0, -1,  0),
        (1,  0,  0),
        (-1, 0,  0),
    ]

    return sum(1 for x, y, z in cubes for nx, ny, nz in neighbours if (x+nx, y+ny, z+nz) not in cubes)


def part2(data):
    cubes = set(data)
    edges = set()

    neighbours = [
        (0,  0,  1),
        (0,  0, -1),
        (0,  1,  0),
        (0, -1,  0),
        (1,  0,  0),
        (-1, 0,  0),
    ]

    # Construct a bounding box around the obsidian shape
    def get_min_max(axis, cubes):
        ns = [cube[axis] for cube in cubes]
        return min(ns) - 1, max(ns) + 1

    min_x, max_x = get_min_max(0, cubes)
    min_y, max_y = get_min_max(1, cubes)
    min_z, max_z = get_min_max(2, cubes)

    def add_points(x1, y1, z1, x2, y2, z2):
        return (x1+x2, y1+y2, z1+z2)

    def is_in_bounds(x, y, z):
        return min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z

    # Flood fill the bounding box and keep track of seen edges
    queue = [(min_x, min_y, min_z)]
    seen = set(queue[0])
    while len(queue) > 0:
        point = queue.pop(0)
        for neighbour in neighbours:
            new_point = add_points(*point, *neighbour)

            if new_point in cubes:
                edges.add((point, new_point))
                continue

            if new_point not in seen and is_in_bounds(*new_point):
                seen.add(new_point)
                queue.append(new_point)

    return len(edges)


if __name__ == "__main__":
    main()
