import time
start_time = time.time()

instructions = [(x[:3], x.rstrip()[4:]) for x in open("input-08.txt").readlines()]

accumulator = 0
counter = 0
executed = []


while True:
    if counter in executed:
        print("Part 1:", accumulator)
        break
    
    executed.append(counter)
    op, arg = instructions[counter]
    if op == 'nop':
        counter += 1
        continue
    elif op == 'jmp':
        counter += int(arg)
        continue
    elif op == 'acc':
        accumulator += int(arg)
        counter += 1
        continue
    else:
        print('unknown operation')
        break





test_op = 0
found = False

while not found:
    accumulator = 0
    counter = 0
    executed = []

    while True:
        if counter > len(instructions):
            found = True
        if counter in executed:
            test_op += 1
            break
        
        executed.append(counter)
        try:
            op, arg = instructions[counter]
        except IndexError:
            found = True
            print("Part 2:", accumulator)
            break

        if counter == test_op:
            if op == 'nop':
                op = 'jmp'
            elif op == 'jmp':
                op = 'nop'

        if op == 'nop':
            counter += 1
            continue
        elif op == 'jmp':
            counter += int(arg)
            continue
        elif op == 'acc':
            accumulator += int(arg)
            counter += 1
            continue
        else:
            print('unknown operation')
            break

end_time = round((time.time() - start_time) * 1000, 2)
print(f"Solved in: {end_time}ms" )