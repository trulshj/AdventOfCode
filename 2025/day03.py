import utils.aoc as aoc


def find_max_joltage(bank: list[int], batteries: int):
    joltage = 0
    for i in range(batteries, 1, -1):
        max_digit = max(bank[:-(i-1)])
        joltage += max_digit * 10**(i-1)
        bank = bank[bank.index(max_digit)+1:]
    return joltage + max(bank)


banks = [list(map(int, x.rstrip())) for x in aoc.readlines()]
print("Part 1:", sum(find_max_joltage(bank, 2) for bank in banks))
print("Part 2:", sum(find_max_joltage(bank, 12) for bank in banks))
