from collections import deque, defaultdict
import itertools
from tqdm import tqdm


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def next_secret(secret):
    a = prune(mix(secret, secret * 64))
    b = prune(mix(a, a // 32))
    return prune(mix(b, b * 2048))


def get_nth_secret(secret):
    for _ in range(2000):
        secret = next_secret(secret)
    return secret


def get_price_sequence(secret):
    changes = deque()
    stuff = []
    old_price = secret % 10
    for _ in range(2000):
        secret = next_secret(secret)
        price = secret % 10
        difference = price - old_price
        old_price = price

        changes.append(difference)
        if len(changes) > 4:
            changes.popleft()

        stuff.append((tuple(changes), price))

    c = defaultdict(int)
    for change, price in stuff[::-1]:
        c[change] = price
    return c


x = (1, 2, 3)

with open("2024/input22.txt") as f:
    initial_secrets = list(map(int, f.read().split()))


print(sum(map(get_nth_secret, initial_secrets)))

sequences = list(map(get_price_sequence, initial_secrets))


def is_valid_changes(changes):
    lower, upper = 0, 9
    for c in changes:
        lower = max(lower+c, 0)
        upper = min(upper+c, 9)
        if lower > upper:
            return False
    return True


max_price = float("-inf")
for target in filter(is_valid_changes, itertools.product(range(-9, 10), repeat=4)):
    price = sum(map(lambda x, target=target: x[target], sequences))
    max_price = max(price, max_price)
print(max_price)
