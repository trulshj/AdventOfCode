from tqdm import tqdm

with open("2024/input09.txt") as f:
    disk_map = list(map(int, f.read().rstrip()))


def create_blocks(disk_map):
    return [(idx//2 if idx % 2 else None, int(size))
            for idx, size in enumerate(disk_map, 1)]


def create_disk(disk_map):
    disk = []
    for block_id, size in create_blocks(disk_map):
        for _ in range(size):
            disk.append((block_id, 1))
    return disk


def defrag(disk):
    for i in tqdm(range(len(disk))[::-1]):
        for j in range(i):
            i_id, i_size = disk[i]
            j_id, j_size = disk[j]

            if i_id != None and j_id == None and i_size <= j_size:
                disk[i] = (None, i_size)
                disk[j] = (None, j_size-i_size)
                disk.insert(j, (i_id, i_size))


def generate_disk_image(disk):
    return [x for y in ([data]*size for data, size in disk) for x in y]


def checksum(disk):
    total = 0
    for i, e in enumerate(disk):
        if e:
            total += i * e
    return total


def flatten(x): return [item for sublist in x for item in sublist]


def part1():
    disk = create_disk(disk_map)
    defrag(disk)
    disk_image = generate_disk_image(disk)
    print("Part 1:", checksum(disk_image))


def part2():
    blocks = create_blocks(disk_map)
    defrag(blocks)
    disk_image = generate_disk_image(blocks)
    print("Part 2:", checksum(disk_image))


if __name__ == "__main__":
    part1()
    part2()
