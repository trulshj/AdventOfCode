import itertools


def main():
    with open('inputs/day17.txt') as f:
        containers = [int(x.rstrip()) for x in f.readlines()]

    LITERS = 150

    ways = 0
    min_container_ways = None
    for i in range(len(containers)):
        sub = 0
        for combination in itertools.combinations(containers, i):
            if sum(combination) == LITERS:
                sub += 1
        if min_container_ways == None and sub > 0:
            min_container_ways = sub
        ways += sub

    print("Part: 1", ways)
    print("Part: 2", min_container_ways)


if __name__ == "__main__":
    main()
