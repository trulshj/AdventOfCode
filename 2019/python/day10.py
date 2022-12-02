
import math

# Parse and format the input
lines = []
for line in open("input.txt").readlines():
    lines.append([x for x in line.rstrip()])

asteroids = []
for y, l in enumerate(lines):
    for x, a in enumerate(l):
        if a == '#':
            asteroids.append((y, x))

# Part 1
# For each asteroid, check how many asteroids are at an unique angle to it
max_seen = 0
for current_a in asteroids:
    current_seen = 0
    angles_seen = []
    for a in asteroids:
        y = a[0] - current_a[0]
        x = a[1] - current_a[1]
        angle = math.atan2(y, x)
        if angle not in angles_seen:
            current_seen += 1
            angles_seen.append(angle)
    # If an asteroid can see more asteroids than the ones before it, save it for later
    if current_seen > max_seen:
        max_seen = current_seen
        station = current_a

# How many asteroids can our station see?
part1 = max_seen


# Part 2
# Remove the station from our list of meteors, we don't want to destroy that one
asteroids.remove(station)


# Returns the distance of a point to our station
def distance(point):
    vector = [point[1] - station[1], point[0] - station[0]]
    return math.hypot(vector[0], vector[1])


# Returns the clockwise angle from straight up to our station
def clockwiseangle(point):
    # Reference vector that goes straight up
    ref_v = [0, 1]
    v = [point[1] - station[1], point[0] - station[0]]
    # Find the length of the vector
    lenvector = distance(v)
    # Normalize the vector
    v = [v[0] / lenvector, v[1] / lenvector]
    # Find dot and diff product
    dotprod = v[0] * ref_v[0] + v[1] * ref_v[1]
    diffprod = ref_v[1] * v[0] - ref_v[0] * v[1]
    # Find direction aware angle
    ca = math.atan2(diffprod, dotprod)
    # We don't want negative angles, we just want to go clockwise
    if ca < 0:
        ca = 2 * math.pi + ca
    return ca


# Distance and angle for sorting purposes
def distance_angle(point):
    d = distance(point)
    ca = clockwiseangle(point)
    return ca, d


# Sort asteroids by clockwise angle and distance (we should vaporize the closest ones first)
asteroids.sort(key=distance_angle)

vaporized = 0
while asteroids:
    angles_seen = []
    for a in asteroids:
        angle = clockwiseangle(a)
        if angle not in angles_seen:
            asteroids.remove(a)
            angles_seen.append(angle)
            vaporized += 1
            if vaporized == 200:
                part2 = a


part2 = part2[1] * 100 + part2[0]
print(part2)
