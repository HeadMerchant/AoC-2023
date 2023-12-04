from math import prod

schematic = [line.strip() for line in open("input.txt").readlines()]

symbols = [
    (r, c)
        for r, row in enumerate(schematic)
        for c, col in enumerate(row)
        if col == '*'
]

rows = len(schematic)
def neighbors(r, c):
    for y in range(-1, 2):
        for x in range(-1, 2):
            row = r+y
            col = c+x
            if (row, col) == (r, c):
                continue
            if 0 <= row < rows and 0 <= col < len(schematic[row]):
                yield (row, col)


def first_digit_index(row, c):
    for c in range(c-1, -1, -1):
        if not row[c].isdigit():
            return c+1
    return c

def last_digit_index(row, c):
    for c in range(c+1, len(row)):
        if not row[c].isdigit():
            return c-1
    return c
      
# row, col: start, end (inclusive)
part_numbers = {}

numbers = []

total = 0
for r, c in symbols:
    for row, col in neighbors(r, c):
        if (row, col) in part_numbers:
            continue
        
        char = schematic[row][col]
        if char.isdigit():
            start = first_digit_index(schematic[row], col)
            end = last_digit_index(schematic[row], col)

            part_numbers.update({
                (row, col): (start, end)
                for col in range(start, end+1)
            })
        elif char != '.':
            # debug
            print(f"Rejecting {row, col} char: {schematic[row][col]}")


total = 0
for r, c in symbols:
    gear_numbers = {}
    for row, col in neighbors(r, c):
        if (row, col) in part_numbers:
            start, end = part_numbers[(row, col)]
            gear_numbers[(row, start)] = end
        else:
            char = schematic[row][col]
            if char != '.':
                pass

    if len(gear_numbers) == 2:
        total += prod((
            int(schematic[row][start:end+1]) for (row, start), end in gear_numbers.items()
        ))

print(total)
