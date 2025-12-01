
wires = {}
gates = []
done = []

with open("2024/input24.txt") as f:
    a, b = f.read().split("\n\n")
    for line in a.splitlines():
        wire, value = line.split(": ")
        wires[wire] = int(value)

    for line in b.splitlines():
        a, op, b, _, out = line.split()
        gates.append((a, op, b, out))
        done.append(False)


def solve(wires, gates):
    done = [False] * len(wires)
    while not all(done):
        for idx, (a, op, b, out) in enumerate(gates):
            if done[idx] or not (a in wires and b in wires):
                continue

            a_val = wires[a]
            b_val = wires[b]

            match op:
                case "AND":
                    wires[out] = a_val & b_val
                case "OR":
                    wires[out] = a_val | b_val
                case "XOR":
                    wires[out] = a_val ^ b_val

            done[idx] = True


x_wires = []
y_wires = []
z_wires = []

for wire in wires.keys():
    match wire[0]:
        case 'x': x_wires.append(wire)
        case 'y': y_wires.append(wire)
        case 'z': z_wires.append(wire)

print(len(x_wires))
print(len(y_wires))
print(len(z_wires))

out = ""
for wire in sorted(filter(lambda w: w[0] == 'z', wires.keys()), reverse=True):
    out += str(wires[wire])
print(int(out, 2))
