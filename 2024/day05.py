from collections import defaultdict


with open("2024/input05.txt") as f:
    a, b = f.read().split("\n\n")
    rules = [tuple(map(int, x.rstrip().split("|"))) for x in a.split("\n")]
    orderings = [list(map(int, x.split(","))) for x in b.split()]

lookup = defaultdict(list)
for rule in rules:
    lookup[rule[0]].append(rule[1])


def check_validity(ordering):
    valid = True
    for i in range(len(ordering)-1, 0, -1):
        if not valid:
            break
        for j in range(i):
            if ordering[j] in lookup[ordering[i]]:
                valid = False
                break
    return valid


total = 0
incorrect_orderings = []

for ordering in orderings:
    if check_validity(ordering):
        total += ordering[len(ordering) // 2]
    else:
        incorrect_orderings.append(ordering)

print("Part 1:", total)

fixed_total = 0
for ordering in incorrect_orderings:
    while not check_validity(ordering):
        for i in range(len(ordering)-1, 0, -1):
            for j in range(i):
                if ordering[j] in lookup[ordering[i]]:
                    ordering.insert(i, ordering.pop(j))

    fixed_total += ordering[len(ordering) // 2]

print("Part 2:", fixed_total)
