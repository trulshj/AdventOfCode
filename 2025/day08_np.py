import utils.aoc as aoc
from math import prod
from collections import defaultdict
import numpy as np

timer = aoc.start()

boxes = [tuple(map(int, l.split(","))) for l in aoc.lines()]
n = len(boxes)

coords = np.array(boxes, dtype=np.int64)

sq = np.sum(coords * coords, axis=1, keepdims=True)
dist2 = sq - 2 * (coords @ coords.T) + sq.T

i_idx, j_idx = np.triu_indices(n, k=1)
flat_dist = dist2[i_idx, j_idx]
order = np.argsort(flat_dist)

box_to_group = {i: i for i in range(n)}
group_to_boxes = defaultdict(set, ((i, {i}) for i in range(n)))

part1_done = False

for idx, edge_pos in enumerate(order):
    ai = int(i_idx[edge_pos])
    bi = int(j_idx[edge_pos])

    a_group = box_to_group[ai]
    b_group = box_to_group[bi]

    if a_group == b_group:
        continue

    a_boxes = group_to_boxes[a_group]
    b_boxes = group_to_boxes.pop(b_group)

    for v in b_boxes:
        box_to_group[v] = a_group

    a_boxes.update(b_boxes)

    if not part1_done and idx == 999:
        sizes = sorted((len(g) for g in group_to_boxes.values()), reverse=True)
        aoc.p1(prod(sizes[:3]))
        part1_done = True

    if len(group_to_boxes) == 1:
        a = boxes[ai]
        b = boxes[bi]
        aoc.p2(a[0] * b[0])
        break

timer.stop().print()
