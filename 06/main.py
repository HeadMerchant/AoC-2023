import re
import math
lines = [line.strip() for line in open("input.txt").readlines()]

def split(line):
    return [int(x) for x in line.split(" ") if x.isnumeric()]
records = split(lines[0])
dists = split(lines[1])

def concat(line):
    nums = (x for x in line.split(" ") if x.isnumeric())
    return int("".join(nums))
total = 1

for r, d in zip(records, dists):
    disc = r*r - 4*d
    if disc < 0:
        continue

    max_hold = (r + math.sqrt(disc)) / 2
    min_hold = (r - math.sqrt(disc)) / 2

    total *= 1 + math.floor(max_hold) - math.ceil(min_hold)

r = concat(lines[0])
d = concat(lines[1])
disc = r*r - 4*d

max_hold = (r + math.sqrt(disc)) / 2
min_hold = (r - math.sqrt(disc)) / 2

ways = 1 + math.floor(max_hold) - math.ceil(min_hold)
    

print(f"Part 1: {total}")
print(f"Part 2: {ways}")