from dataclasses import dataclass
from math import lcm


@dataclass
class Module:
    module_type: str
    name: str
    destinations: list[str]


FLIP_FLOP = '%'
CONJUNCTION = '&'
BROADCASTER = 'b'

modules: dict[str, Module] = {}
flip_flop_states = {}
conjunction_states = {}

with open('./input20.txt') as f:
    for line in f.readlines():
        module, destinations = line.strip().split(' -> ')
        module_type = module[0]
        name = module[1:] if not module[1:].endswith(
            'roadcaster') else 'broadcaster'
        destinations = destinations.split(', ')
        modules[name] = Module(
            module_type, name, destinations)
        if module_type == FLIP_FLOP:
            flip_flop_states[name] = False
        elif module_type == CONJUNCTION:
            conjunction_states[name] = {}

for con_module in conjunction_states.keys():
    for other in modules.values():
        if con_module in other.destinations:
            conjunction_states[con_module][other.name] = False

LOW_PULSE = False
HIGH_PULSE = True

low_pulses = 0
high_pulses = 0
button_presses = 0


def button_press():
    return [(name, LOW_PULSE, 'broadcaster') for name in modules['broadcaster'].destinations]


queue = []

watch = ['cl', 'rp', 'lb', 'nj']

presses = {name: [] for name in watch}

for _ in range(10_000):
    if button_presses == 1000:
        print(f"Product of low and high pulses: {low_pulses * high_pulses}")

    queue += button_press()
    low_pulses += 1
    button_presses += 1

    while (queue):
        name, pulse_type, origin = queue.pop(0)

        if pulse_type == HIGH_PULSE:
            high_pulses += 1
        else:
            low_pulses += 1

        if name not in modules:
            continue

        module = modules[name]

        if module.module_type == BROADCASTER:
            queue += [(dest, pulse_type, name) for dest in module.destinations]
            continue

        if module.module_type == FLIP_FLOP:
            if pulse_type == HIGH_PULSE:
                continue

            state = flip_flop_states[name]
            flip_flop_states[name] = not state
            queue += [(dest, not state, name) for dest in module.destinations]
            continue

        if module.module_type == CONJUNCTION:
            conjunction_states[name][origin] = pulse_type
            next_type = not all(conjunction_states[name].values())
            if name in watch and next_type:
                presses[name].append(button_presses)
                if len(presses) == len(watch) and all([len(x) == 2 for x in presses.values()]):
                    periods = 1
                    for x in presses.values():
                        diff = x[1] - x[0]
                        periods = lcm(periods, diff)
                    print("First low to rx found at: ", periods)
                    exit()

            queue += [(dest, next_type, name) for dest in module.destinations]
