import itertools


def part1(data):
    return None


def part2(data):
    return None


def main():
    towns = set()
    distances = {}

    with open('inputs/day09.txt') as f:
        for line in f.readlines():
            t1, _, t2, _, distance = line.rstrip().split()
            distances[(t1, t2)] = int(distance)
            distances[(t2, t1)] = int(distance)
            towns.add(t1)
            towns.add(t2)

    town_permutations = list(itertools.permutations(towns))
    route_lengths = []

    for perm in town_permutations:
        length = 0

        for i in range(len(perm) - 1):
            length += distances[(perm[i], perm[i+1])]

        route_lengths.append(length)

    print("Part 1:", min(route_lengths))
    print("Part 2:", max(route_lengths))


if __name__ == "__main__":
    main()
