from math import inf

arrival_time, buses = open("input-13.txt").read().split('\n')
arrival_time = int(arrival_time)

buses = [b for b in buses.split(',')]
in_service = [int(b) for b in buses if b != 'x']


lowest_waiting_time = inf
bus_to_catch = 0

for bus in in_service:
    waiting_time = ((arrival_time // bus) + 1) * bus - arrival_time

    if waiting_time < lowest_waiting_time:
        lowest_waiting_time = waiting_time
        bus_to_catch = bus


print("Part 1:", bus_to_catch * lowest_waiting_time)


timestamp = 0
running_product = 1

for idx, bus in enumerate(buses):
    if bus == 'x':
        continue
    while (timestamp + idx) % int(bus) != 0:
        timestamp += running_product
    running_product *= int(bus)
print("Part 2:", timestamp)
