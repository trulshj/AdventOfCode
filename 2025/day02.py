with open("2025/input02.txt") as f:
    ranges = [tuple(map(int, x.split("-")))
              for x in f.read().rstrip().split(",")]


def is_invalid1(s: str):
    return len(s) % 2 == 0 and s.startswith(s[len(s)//2:])


def is_invalid2(s: str):
    return len(s) > 1 and s in (s + s)[1:-1]


numbers = [n for low, high in ranges for n in range(low, high+1)]
invalid_sum1 = sum(n for n in numbers if is_invalid1(str(n)))
invalid_sum2 = sum(n for n in numbers if is_invalid2(str(n)))

print("Part 1:", invalid_sum1)
print("Part 2:", invalid_sum2)
