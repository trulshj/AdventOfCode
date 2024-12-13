import re
with open("2024/input13.txt") as f:
    equations = [tuple(map(int, re.findall(r"\d+", e)))
                 for e in f.read().split("\n\n")]

p1 = p2 = 0
ADJUSTMENT = 10_000_000_000_000


def solve(ax, ay, bx, by, px, py, adjustment=0):
    px += adjustment
    py += adjustment

    s = (px*by - py*bx) / (ax*by-ay*bx)
    t = (px-ax*s) / bx

    if int(s) != s:
        return 0

    return s * 3 + t


for equation in equations:
    p1 += solve(*equation)
    p2 += solve(*equation, ADJUSTMENT)

print(int(p1))
print(int(p2))
