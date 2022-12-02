from collections import Counter


def has_vowels(string):
    vowels = "aeiou"
    vowel_count = 0
    for c in string:
        if c in vowels:
            vowel_count += 1

    return vowel_count >= 3


def has_disallowed(string):
    disallowed_combinations = ["ab", "cd", "pq", "xy"]
    for i in range(len(string)):
        pair = string[i:i+2]

        if pair in disallowed_combinations:
            return True
    return False


def has_double(string):
    for i in range(len(string)):
        pair = string[i:i+2]

        if len(pair) > 1 and pair[0] == pair[1]:
            return True
    return False


def part1(data):
    nice_count = 0
    for string in data:
        if has_double(string) and has_vowels(string) and not has_disallowed(string):
            nice_count += 1
    return nice_count


def has_double_pair(string):
    pairs = tuple(zip(string, string[1:]))
    for i in range(len(pairs)):
        for j in range(i+2, len(pairs)):
            if pairs[i] == pairs[j] and i < j:
                return True
    return False


def has_fork(string):
    triples = tuple(zip(string, string[1:], string[2:]))
    for x in triples:
        if x[0] == x[2]:
            return True
    return False


def part2(data):
    nice_count = 0
    for string in data:
        if has_double_pair(string) and has_fork(string):
            nice_count += 1
    return nice_count


def main():
    with open('inputs/day05.txt') as f:
        data = [x.rstrip() for x in f.readlines()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
