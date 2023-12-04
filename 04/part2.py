# completed 12:14

cards = [line.strip() for line in open("input.txt").readlines()]

def split_nums(num_string):
    return set((int(num) for num in num_string.split(" ") if num))


total = 0
copies = [1] * len(cards)

for i, (card, copy_count) in enumerate(zip(cards, copies)):
    _, numbers = card.split(": ")
    winning, have = numbers.split(" | ")
    
    winning = split_nums(winning)
    have = split_nums(have)

    match = winning & have
    
    for j in range(i+1, i+len(match)+1):
        copies[j] += copy_count


print(sum(copies))

