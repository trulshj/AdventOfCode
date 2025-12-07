import utils.aoc as aoc

h, t = aoc.sections()
ranges = [tuple(map(int, x.split('-'))) for x in h]
ingredients = [int(x) for x in t]


fresh = 0
for ingredient in ingredients:
    for start, end in ranges:
        if start <= ingredient <= end:
            fresh += 1
            break

print(fresh)


def collapse(ranges):
    ranges.sort(key=lambda x: x[0])

    collapsed = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        collapsed_start, collapsed_end = collapsed[-1]

        if current_start <= collapsed_end:
            collapsed[-1] = (collapsed_start, max(collapsed_end, current_end))
        else:
            collapsed.append((current_start, current_end))

    return collapsed


def size(range):
    return range[1] - range[0] + 1


print(sum(map(size, collapse(ranges))))
