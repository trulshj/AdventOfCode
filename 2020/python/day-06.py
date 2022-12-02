
def check_group_answers(group):
    answers = [c for person in group for c in person]
    return len(set(answers))


def intersection(list1, list2):
    return [val for val in list1 if val in list2]


def group_intersection(group):
    answers = [c for c in group[0]]
    for person in group:
        answers = intersection(answers, [c for c in person])
    return len(set(answers))


groups = [x.split('\n') for x in (open("input-06.txt").read()).split('\n\n')]

print(f"Part 1: {sum([check_group_answers(group) for group in groups])}")
print(f"Part 2: {sum([group_intersection(group) for group in groups])}")
