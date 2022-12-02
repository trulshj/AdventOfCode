
import time
start_time = time.time()

data = [int(i) for i in open("input.txt").read()]

# Part 1
w, h = 25, 6
layers = []

# Split the input into the image layers
while len(data) > 0:
    layer = data[:w*h]
    layers.append(layer)
    data = data[w*h:]


fewest_layer = []
fewest_count = w * h

# Find the layers with the fewest zeroes
for layer in layers:
    if layer.count(0) < fewest_count:
        fewest_count = layer.count(0)
        fewest_layer = layer

# Get the checksum
part1 = fewest_layer.count(1) * fewest_layer.count(2)


# Part 2
final_image = []
for x in range(w*h):
    final_image.append('.')

# Stack the layers appropriately and find final pixel value
for layer in layers:
    for i, p in enumerate(layer):
        if p == 0 and final_image[i] == '.':
            final_image[i] = ' '
        elif p == 1 and final_image[i] == '.':
            final_image[i] = '#'

# Stop the timer
stop_time = time.time() - start_time

print(" Day 8 ".center(64, '-'))
print(f"Checksum for image data: {part1}".center(64))
print("Final image:".center(64))
while len(final_image) > 0:
    print(" ".join(final_image[:w]).center(64))
    final_image = final_image[w:]
print("".center(64, '-'))
print(f"Found in {round(stop_time, 7)} seconds".center(64))
