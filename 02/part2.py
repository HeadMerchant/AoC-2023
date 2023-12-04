from collections import Counter
import math
lines = open('input.txt')

pieces = Counter({
    'red': 12,
    'green': 13,
    'blue': 14
})
id_sum = 0
total_power = 0
for game_id, line in enumerate(lines.readlines()):
    line = line.strip()
    game_id += 1
    
    _, line = line.split(': ')
    groups = line.split('; ')
    min_counts = Counter()
    for group in groups:
        counts = group.split(', ')
        counts = Counter({
            color: int(count) for (count, color) in map(lambda x: x.split(' '), counts)
        })

        min_counts |= counts

    total_power += math.prod((min_counts.values()))


print(total_power)
