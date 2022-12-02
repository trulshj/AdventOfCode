
code = [int(n) for n in open("input.txt").read().split(",")]


def evaluate(noun, verb):
    t = [n for n in code]
    t[1] = noun
    t[2] = verb
    c = 0
    while True:
        op = t[c]
        i1, i2, i3 = t[c + 1], t[c + 2], t[c + 3]
        if op == 1:
            t[i3] = t[i1] + t[i2]
        elif op == 2:
            t[i3] = t[i1] * t[i2]
        else:
            break
        c += 4
    return t[0]


# Pretty print
print(" Day 2 ".center(64, "-"))

# Part 1
print(f"Output after code 1202: {evaluate(12, 2)}".center(64))

# Part 2
for x in range(100):
    for y in range(100):
        if evaluate(x, y) == 19690720:
            print(f"Checksum: {100 * x + y}".center(64))

# More pretty print
print("".center(64, "-"))
