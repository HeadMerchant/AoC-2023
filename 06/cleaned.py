import math
lines = [line.strip() for line in open("input.txt").readlines()]

def split(line):
    return [int(x) for x in line.split(" ") if x.isnumeric()]

def solve(r, d):
    disc = r*r - 4*d
    if disc < 0:
        return 1 # hack for iterator

    max_hold = (r + math.sqrt(disc)) / 2
    min_hold = (r - math.sqrt(disc)) / 2
    return 1 + math.floor(max_hold) - math.ceil(min_hold)

total = math.prod(solve(r, d) for r, d in zip(split(lines[0], lines[1])))

def concat(line):
    nums = (x for x in line.split(" ") if x.isnumeric())
    return int("".join(nums))

ways = concat(lines[0]), concat(lines[1])

print(f"Part 1: {total}")
print(f"Part 2: {solve(*ways)}")