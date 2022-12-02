import re


def increment_string(string: str) -> str:
    if len(string) == 0:
        return ''

    remainder, last = string[:-1], string[-1]
    if last == 'z':
        return increment_string(remainder) + 'a'
    else:
        return remainder + chr(ord(last) + 1)


def has_straight(string: str):
    for i in range(len(string) - 2):
        a = ord(string[i])
        b = ord(string[i+1])
        c = ord(string[i+2])
        if c - b == 1 and b - a == 1:
            return True
    return False


def has_iol(string: str):
    return re.match(r"[iol]", string) == None


def has_double(string: str):
    return len(re.findall(r"(.)\1", string)) >= 2


def find_next_password(data):
    while not has_iol(data) or not has_straight(data) or not has_double(data):
        data = increment_string(data)
    return data


def main():
    with open('inputs/day11.txt') as f:
        data = f.readline().rstrip()

    print(password := find_next_password(data))
    print(find_next_password(increment_string(password)))


if __name__ == "__main__":
    main()
