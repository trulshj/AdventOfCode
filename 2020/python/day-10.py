
adapters = sorted([int(x.rstrip()) for x in open("input-10.txt").readlines()])
adapters = [0, *adapters, (adapters[-1] + 3)]
differences = {1: 0, 2: 0, 3: 0}

for idx, val in enumerate(adapters[:-1]):
    diff = adapters[idx+1] - adapters[idx]
    differences[diff] += 1

print("Part 1:", differences[1] * differences[3])


ways = {0: 1}
for adapter in sorted(adapters[1:]):
    ways[adapter] = ways.get(adapter - 1, 0) + ways.get(adapter - 2, 0) + ways.get(adapter - 3, 0)
print("Part 2:", ways[adapters[-1]])
