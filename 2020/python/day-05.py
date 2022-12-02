
def check_pass(b_pass):
    id = 0
    for i, c in enumerate(b_pass[::-1]):
        if c == 'B' or c == 'R':
            id += 2 ** i
    return id


boarding_passes = [x.rstrip() for x in open("input-05.txt").readlines()]
pass_ids = set([check_pass(b_pass) for b_pass in boarding_passes])

print(f"Part 1: {max(pass_ids)}")

for id in pass_ids:
    if id+1 not in pass_ids and id+2 in pass_ids:
        print(f"Part 2: {id+1}")
