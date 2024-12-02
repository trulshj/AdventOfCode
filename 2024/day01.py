from collections import Counter


def read_input():
    with open("./input01.txt") as f:
        return [x.rstrip().split() for x in f.readlines()]
    

x = read_input()

left_list = sorted(int(e[0]) for e in x)
right_list = sorted(int(e[1]) for e in x)

print(sum(map(lambda x: abs(x[0] - x[1]), zip(left_list, right_list))))


occurences = Counter(right_list)
similarity = 0
for n in left_list:
    similarity += n * occurences[n]
    
print(similarity)