from collections import defaultdict

connections = defaultdict(set)

with open("2024/input23.txt") as f:
    for c1, c2 in (x.rstrip().split('-') for x in f.readlines()):
        connections[c1].add(c2)
        connections[c2].add(c1)


def find_loops(node: str):
    loops = set()
    for n in connections[node]:
        for m in connections[n] - {node}:
            for o in connections[m]:
                if o == node:
                    loops.add(tuple(sorted([n, m, o])))
    return loops


total_loops = set()
for node in connections:
    total_loops.update(find_loops(node))


def has_t_computer(loop):
    return any(map(lambda x: x[0] == 't', loop))


print(sum(map(has_t_computer, total_loops)))


def find_clique(current: str, conns: set[str]):
    if len(conns) == 1:
        return [current, conns.pop()]
    for node in conns:
        new_connections = conns.intersection(connections[node])
        if len(new_connections) == 0:
            continue
        return [current] + find_clique(node, new_connections)
    return []


longest_clique = []
longest_clique_length = 0
for node in connections:
    clique = find_clique(node, connections[node])
    if len(clique) > longest_clique_length:
        longest_clique = clique
        longest_clique_length = len(clique)
print(','.join(sorted(longest_clique)))
