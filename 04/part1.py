# completed 12:08 eastern

cards = [line.strip() for line in open("input.txt").readlines()]

def split_nums(num_string):
    return set((int(num) for num in num_string.split(" ") if num))


total = 0

for card in cards:
    _, numbers = card.split(": ")
    winning, have = numbers.split(" | ")
    
    winning = split_nums(winning)
    have = split_nums(have)

    match = winning & have
    if match:
        value = 2 ** (len(match) - 1)
        total += value

print(total)
