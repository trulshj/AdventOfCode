
data = [x.rstrip() for x in open("input03.txt").readlines()]


def part1(data):
    digits = [list(map(int, x)) for x in data]
    counts = list(map(sum, zip(*digits)))
            
    gamma_rate = ""
    epsilon_rate = ""
    for i in counts:
        if i > len(digits) / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
            
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    
    return gamma_rate * epsilon_rate


def part2(data):
    digits = [list(map(int, x)) for x in data]

    oxygen = digits
    c02 = digits
    
    for i in range(len(digits[0])):
        oxygen_counts = list(map(sum, zip(*oxygen)))
        c02_counts = list(map(sum, zip(*c02)))
        
        if (len(oxygen) > 1):
            if oxygen_counts[i] >= (len(oxygen) / 2):
                oxygen = [x for x in oxygen if x[i] == 1]
            else:
                oxygen = [x for x in oxygen if x[i] == 0]   
            
        if (len(c02) > 1):
            if c02_counts[i] >= (len(c02) / 2):
                c02 = [x for x in c02 if x[i] == 0]   
            else:
                c02 = [x for x in c02 if x[i] == 1]
            
    oxygen = int(''.join([str(x) for x in oxygen[0]]), 2)
    c02 = int(''.join([str(x) for x in c02[0]]), 2)
    
    return oxygen * c02

    
if __name__ == "__main__":
    print("--- AOC Day 03 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
