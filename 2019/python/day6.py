
import time
start_time = time.time()

orbits = [line.rstrip().split(')') for line in open("input.txt").readlines()]
planets = {'COM': []}

num = 0

# Make a dictionary of the orbits
for parent, child in orbits:
    if child not in planets.keys():
        planets[child] = []
    planets[child].append(parent)


def get_orbits(p):
    global num
    if planets[p] == 'COM':  # if we are at the center of mass, stop
        num += 1
        return
    num += 1  # This is an orbit, so count it
    for suborbit in planets[p]:  # Now count all the indirect orbits
        get_orbits(suborbit)


# Get the number of orbits for each planet
for planet in planets:
    get_orbits(planet)

# For some reason the planets themselves get counted as orbits, just subtract this
part1 = num - len(planets)


together = False
you, san = planets['YOU'], planets['SAN']
visited_santa = []
visited_you = []

while True:
    if san in visited_you:
        part2 = (visited_you.index(san) + len(visited_santa))
        break
    else:
        visited_santa.append(san)
        san = planets[san[0]]
    if you in visited_santa:
        part2 = (visited_santa.index(you) + len(visited_you))
        break
    else:
        visited_you.append(you)
        you = planets[you[0]]

print(" Day 6 ".center(64, '-'))
print(f"Total number of direct and indirect orbits: {part1}".center(64))
print(f"Total number of gravity transfers needed: {part2}".center(64))
print("".center(64, '-'))
print(f"Found in {round((time.time() - start_time), 5)} seconds".center(64))
