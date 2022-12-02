def run_program(instructions, registers):
    index = 0
    while True:
        if index >= len(instructions):
            return registers["b"]
        instruction, register, offset = instructions[index]
        if instruction == "hlf":
            registers[register] //= 2
        elif instruction == "tpl":
            registers[register] *= 3
        elif instruction == "inc":
            registers[register] += 1
        elif instruction == "jmp":
            index += int(register)
            continue
        elif instruction == "jie":
            if registers[register] % 2 == 0:
                index += offset
                continue
        elif instruction == "jio":
            if registers[register] == 1:
                index += offset
                continue

        index += 1


def part1(data):
    registers = {"a": 0, "b": 0}
    return run_program(data, registers)


def part2(data):
    registers = {"a": 1, "b": 0}
    return run_program(data, registers)


def main():
    with open('inputs/day23.txt') as f:
        instructions = []
        data = [x for x in f.readlines()]
        for line in data:
            if "," in line:
                line, offset = line.split(", ")
                instruction, register = line.split()
                instructions.append((instruction, register, int(offset)))
            else:
                instruction, register = line.split()
                instructions.append((instruction, register, None))

    print(part1(instructions))
    print(part2(instructions))


if __name__ == "__main__":
    main()
