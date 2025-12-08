import utils.aoc as aoc
from math import prod
from collections import defaultdict
from itertools import combinations

timer = aoc.start()

boxes = [tuple(map(int, l.split(","))) for l in aoc.lines()]

box_to_group = {}
group_to_boxes = defaultdict(set)
for i, box in enumerate(boxes):
    box_to_group[box] = i
    group_to_boxes[i].add(box)


def distance(a, b):
    ax, ay, az = a
    bx, by, bz = b
    dx = ax - bx
    dy = ay - by
    dz = az - bz
    return dx*dx + dy*dy + dz*dz


distances = sorted(
    ((distance(a, b), a, b) for a, b in combinations(boxes, 2)),
    key=lambda x: x[0],
)

timer.stop().print()

connections = 0
part1_done = False

for idx, (_, a, b) in enumerate(distances):
    group_a = box_to_group[a]
    group_b = box_to_group[b]

    if group_a == group_b:
        continue

    if len(group_to_boxes[group_a]) < len(group_to_boxes[group_b]):
        group_a, group_b = group_b, group_a

    a_boxes = group_to_boxes[group_a]
    b_boxes = group_to_boxes.pop(group_b)

    for box in b_boxes:
        box_to_group[box] = group_a

    a_boxes.update(b_boxes)

    if not part1_done and idx == 999:
        sizes = sorted((len(g) for g in group_to_boxes.values()), reverse=True)
        aoc.p1(prod(sizes[:3]))
        part1_done = True

    if len(group_to_boxes) == 1:
        aoc.p2(a[0] * b[0])
        break

timer.stop().print()
