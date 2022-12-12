from utils import print_day

DAY = 12


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return {x + y * 1j: e for y, l in enumerate(f.readlines()) for x, e in enumerate(l.rstrip())}


def is_valid_move(grid, to_point, from_point):
    return (from_point in grid and
            ((grid[to_point] == 'E' and grid[from_point] in ['y', 'z']) or
             (grid[from_point] == 'S' and grid[to_point] in ['a', 'b']) or
             (grid[from_point] != 'S' and grid[to_point] != 'E' and ord(grid[to_point]) - ord(grid[from_point]) <= 1)))


def find_shortes_paths(grid):
    end = [k for k, v in grid.items() if v == 'E'][0]
    shortest_paths = {end: 0}
    queue = [end]

    while queue:
        current = queue.pop(0)
        for neighbor in [current - 1, current + 1, current - 1j, current + 1j]:
            if not neighbor in shortest_paths and is_valid_move(grid, current, neighbor):
                shortest_paths[neighbor] = shortest_paths[current] + 1
                queue.append(neighbor)

    return shortest_paths


def part1(data):
    start = next(k for k, v in data.items() if v == 'S')
    return find_shortes_paths(data)[start]


def part2(data):
    shortest_paths = find_shortes_paths(data)
    return sorted(shortest_paths[p] for p in shortest_paths if data[p] in ['S', 'a'])[0]


if __name__ == "__main__":
    main()
