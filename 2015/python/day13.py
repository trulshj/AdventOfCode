from math import inf
import re
import itertools


def find_happiness(people, changes):
    perms = list(itertools.permutations(people))
    max_happiness = -inf
    for perm in perms:
        happiness = changes[(perm[-1], perm[0])]
        happiness += changes[(perm[0], perm[-1])]

        for i in range(len(perm) - 1):
            happiness += changes[(perm[i], perm[i+1])]
            happiness += changes[(perm[i+1], perm[i])]

        max_happiness = max(max_happiness, happiness)

    return max_happiness


def main():
    people = set()
    changes = {}

    with open('inputs/day13.txt') as f:
        for line in f.readlines():
            n1, t, c, n2 = re.findall(
                r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.", line)[0]
            people.add(n1)
            people.add(n2)
            if t == "gain":
                c = int(c)
            else:
                c = int(c) * -1
            changes[(n1, n2)] = c

    print("Part 1:", find_happiness(people, changes))

    people.add("Myself")
    for person in people:
        changes[(person, "Myself")] = 0
        changes[("Myself", person)] = 0

    print("Part 2:", find_happiness(people, changes))


if __name__ == "__main__":
    main()
