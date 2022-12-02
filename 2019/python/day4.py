
import time
start_time = time.time()

# Range from puzzle input
minimum = 197487
maximum = 673251 + 1


# Check whether the number has similar adjacent digits
def check1(n):
    n = list(str(n))
    if n != sorted(n) or len(set(n)) == len(n):
        return False
    return True


def check2(n):
    return 2 in [str(n).count(d) for d in str(n)]


part1 = [pw for pw in range(minimum, maximum) if check1(pw)]
part2 = len([pw for pw in part1 if check2(pw)])

print()
print(" Day 4 ".center(64, "-"))
print(f"Possible passwords Part 1: {len(part1)}".center(64))
print(f"Possible passwords Part 2: {part2}".center(64))
print("".center(64, "-"))
print(f"Solution found in {time.time() - start_time} seconds".center(64))
