from collections import Counter
lines = open('input.txt')

pieces = Counter({
    'red': 12,
    'green': 13,
    'blue': 14
})
id_sum = 0

for game_id, line in enumerate(lines.readlines()):
    line = line.strip()
    game_id += 1
    
    _, line = line.split(': ')
    groups = line.split('; ')
    for group in groups:
        counts = group.split(', ')
        counts = Counter({
            color: int(count) for (count, color) in map(lambda x: x.split(' '), counts)
        })
        print(f"game {game_id}: {pieces - counts}")

        if any((counts[color] > pieces[color] for color in counts)):
            print(f"break; {game_id}")
            break
    else:
        id_sum += game_id

print(id_sum)
