from collections import Counter


def read_input():
    with open("./input01.txt") as f:
        return [x.rstrip().split() for x in f.readlines()]


pairs = read_input()

left, right = map(sorted, zip(*((int(a), int(b)) for a, b in pairs)))
print(sum(map(lambda x: abs(x[0] - x[1]), zip(left, right))))

occurences = Counter(right)
similarity = 0
for n in left:
    similarity += n * occurences[n]

print(similarity)
