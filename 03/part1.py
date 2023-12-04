import re

schematic = [line.strip() for line in open("input.txt").readlines()]

symbols = [
    (r, c)
        for r, row in enumerate(schematic)
        for c, col in enumerate(row)
        if not (col.isdigit() or col == '.')
]

rows = len(schematic)
# cols = len(schematic[0])
# print(rows, cols)
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
                
seen_indices = set()
# print(schematic[140])

expected = [
    []
]

numbers = []

total = 0
for r, c in symbols:
    for row, col in neighbors(r, c):
        if (row, col) in seen_indices:
            continue
        
        char = schematic[row][col]
        if char.isdigit():
            start = first_digit_index(schematic[row], col)
            end = last_digit_index(schematic[row], col)

            indices = [(row, col) for col in range(start, end+1)]
            # print(indices)
            seen_indices.update(indices)

            part_number = int(schematic[row][start:end+1])
            # print(f"found {part_number}")
            total += part_number

print(total)
