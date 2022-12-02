import time

start_time = time.time()

expense_report = [int(x.rstrip()) for x in open("input-01.txt").readlines()]

print()
print(" Day 1 ".center(64, '-'))

for idx, val1 in enumerate(expense_report):
    for val2 in expense_report[idx+1:]:
        if val1 + val2 == 2020:
            print(f"Part 1: {val1} * {val2} = {val1 * val2}".center(64))

for idx1, val1 in enumerate(expense_report):
    for idx2, val2 in enumerate(expense_report[idx1+1:]):
        for val3 in expense_report[idx2+idx1+1:]:
            if val1 + val2 + val3 == 2020:
                print(
                    f"Part 2: {val1} * {val2} * {val3} = {val1 * val2 * val3}".center(64))

print("\n")
print(f"Found in {time.time() - start_time} seconds".center(64))
print(64 * '-')
