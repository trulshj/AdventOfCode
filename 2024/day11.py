from collections import defaultdict, Counter
from math import log10

with open("2024/input11.txt") as f:
    stones = defaultdict(int, Counter(map(int, f.read().split())))


def digit_count(n: int):
    return int(log10(n)) + 1


def blink(stones: dict[int, int]):
    for stone, amount in list(stones.items()):
        if amount == 0:
            continue
        if stone == 0:
            stones[1] += amount
            stones[stone] -= amount
        elif (digits := digit_count(stone)) % 2 == 0:
            left, right = divmod(stone, 10 ** (digits // 2))
            stones[left] += amount
            stones[right] += amount
            stones[stone] -= amount
        else:
            stones[stone * 2024] += amount
            stones[stone] -= amount


for i in range(25):
    blink(stones)

print("Part 1:", sum(stones.values()))

for i in range(50):
    blink(stones)

print("Part 2:", sum(stones.values()))
