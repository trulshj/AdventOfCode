import re

data = [x.rstrip() for x in open("input-14.txt").readlines()]


def apply_mask(value, mask):
    b_val = str(bin(int(value)))[2:].zfill(36)
    for i in range(len(b_val)):
        if mask[i] != 'X':
            b_val = b_val[:i] + mask[i] + b_val[i+1:]
    return int(b_val, 2)


def find_locations(location, mask):
    locations = []
    
    


memory1 = {}
memory2 = {}
mask = ""


for line in data:
    if line[:4] == "mask":
        mask = line[7:]
    else:
        location, value = re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]
        memory1[location] = apply_mask(value, mask)
        for loc in find_locations(location, mask):
            memory2[loc] = value

print("Part 1:", sum(memory1.values()))
print("Part 2:", sum(memory2.values()))

