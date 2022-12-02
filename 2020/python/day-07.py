import re

lines = [x.rstrip() for x in open("input-07.txt").readlines()]

contains = {}
contained_in = {}

for line in lines:
    sub_bags = re.findall(r"(\d) (\w+ \w+)", line)
    bag = re.findall(r"^\w+ \w+", line)[0]


    for amount, colour in sub_bags:
        if bag not in contains:
            contains[bag] = []
        contains[bag].append([colour, int(amount)])

        if bag not in contained_in:
            contained_in[bag] = []

        if colour not in contains:
            contains[colour] = []

        if colour not in contained_in:
            contained_in[colour] = []
        contained_in[colour].append(bag)


def bfs(colour):
    visited = set()
    queue = [colour]
    while queue:
        current = queue.pop()
        for neighbour in contained_in[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.insert(0, neighbour)
    return visited


def bags_to_fill(colour):
    bags = 0
    for sub_bag in contains[colour]:
        bags += sub_bag[1] * (1 + bags_to_fill(sub_bag[0]))
    return bags


print("Part 1:", len(bfs("shiny gold")))
print("Part 2:", bags_to_fill("shiny gold"))
