from math import log10


equations = []
with open("2024/input07.txt") as f:
    for line in [l.rstrip().split() for l in f.readlines()]:
        target = int(line[0][:-1])
        numbers = list(map(int, line[1:]))
        equations.append((target, numbers))


def ends_with(a: int, b: int):
    return (a - b) % 10 ** digit_count(b) == 0


def digit_count(n: int):
    return int(log10(n)) + 1


def test(target: int, numbers: list[int], use_concatenation=False):
    *head, n = numbers

    if not head:
        return n == target

    q, r = divmod(target, n)
    if r == 0 and test(q, head, use_concatenation):  # '*' op
        return True

    if use_concatenation \
            and ends_with(target, n) \
            and test(target // (10 ** digit_count(n)), head, use_concatenation):  # '||' op
        return True

    return test(target-n, head, use_concatenation)  # '+' op


print("Part 1:",
      sum(target for target, numbers in equations if test(target, numbers)))
print("Part 2:",
      sum(target for target, numbers in equations if test(target, numbers, True)))
