# 9:21
# 9:56

def yield_until_blank():
    for line in lines:
        if line == "":
            return
        yield tuple((int(x) for x in line.split(" ")))

lines = (line.strip() for line in open("input.txt").readlines())

line = next(lines)
_, seeds = line.split(": ")
seeds = [int(seed) for seed in seeds.split(" ")]
seed_ranges = set((seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2))
seeds = set(seeds)
next(lines)

def map_next(in_seeds, in_ranges):
    print(next(lines))
    next_seeds = set()
    next_ranges = set()
    for dst, src, length in yield_until_blank():
        convert = dst - src
        src_end = src + length
        for seed in list(in_seeds):
            if src <= seed < src_end:
                in_seeds.remove(seed)
                next_seeds.add(seed + convert)

        for start, end in list(in_ranges):
            if end <= src or src_end <= start:
                continue
            next_ranges.add((
                max(src, start)+convert,
                min(end, src_end)+convert
            ))

    return next_seeds, next_ranges

# seed_to_soil
# soil_to_fertilizer
# fertilizer_to_water
# water_to_light
# light_to_temperature
# temperature_to_humidity
# humidity_to_location
for _ in range(7):
    seeds, seed_ranges = map_next(seeds, seed_ranges)


print(f"Part 1: {min(seeds)}")
print(f"Part 2: {min(x for x, _ in seed_ranges)}")