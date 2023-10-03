from utils import get_input


def is_valid_triangle(line):
    a, b, c = sorted(map(int, line.split()))
    return a + b > c


def part1(data):
    return sum(1 for line in data if is_valid_triangle(line))


def part2(data):
    total_valid_triangles = 0
    for i in range(0, len(data), 3):
        a1, b1, c1 = data[i].split()
        a2, b2, c2 = data[i+1].split()
        a3, b3, c3 = data[i+2].split()

        t_a = " ".join([a1, a2, a3])
        t_b = " ".join([b1, b2, b3])
        t_c = " ".join([c1, c2, c3])

        total_valid_triangles += sum(1 for t in [t_a, t_b, t_c] if is_valid_triangle(t))

    return total_valid_triangles


def main():
    data = get_input("03").splitlines()
    print(f"🎄 Part 1: {part1(data)}")
    print(f"🎄 Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
