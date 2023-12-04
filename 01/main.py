import sys

def digit1(line, i):
    if line[i].isdigit():
        return int(line[i])
    
    return None

def digit2(line, i):
    digits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    c = line[i]
    if c.isdigit():
        return int(c)
    
    prefix = line[:i+1]
    for key, digit in digits.items():
        if prefix.endswith(key):
            return digit

    return None

def solve(file, get_digit):
    total = 0
    first = 0
    last = 0
    
    for line in file.readlines():
        for i, _ in enumerate(line):
            d = get_digit(line, i)
            if d is not None:
                first = d
                break

        for i, _ in enumerate(line):
            d = get_digit(line, i)
            if d is not None:
                last = d
        
        total += first*10 + last
    print(total)

if sys.argv[1] == '1':
    solve(open('input.txt'), digit1)
else:
    solve(open('input.txt'), digit2)