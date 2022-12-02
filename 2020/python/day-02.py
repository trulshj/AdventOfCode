import time
import re

start_time = time.time()
print()
print(" Day 2 ".center(48, '-'))

valid_passwords_1 = 0
valid_passwords_2 = 0

for line in open("input-02.txt").readlines():
    match = re.search(r'^(\d+)-(\d+) (\w): (\w+)', line)
    min, max, char, password = match.groups()
    min = int(min)
    max = int(max)

    policy_1 = min <= password.count(char) <= max
    policy_2 = (password[min-1] == char) ^ (password[max-1] == char)
    
    if policy_1:
        valid_passwords_1 += 1
    if policy_2:
        valid_passwords_2 += 1


print(f"Part 1: {valid_passwords_1}".center(48))
print(f"Part 2: {valid_passwords_2}".center(48))
print("\n")
print(f"Found in {time.time() - start_time} seconds".center(48))
print(48 * '-')
