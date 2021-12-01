from common import parse

FILENAME = "day1.txt"

def puzzle1(data):
    counter = 0
    i = 1
    while (i < len(data)):
        if data[i] > data[i-1]:
            counter += 1
        i += 1
    return counter

def puzzle2(data):
    counter = 0
    prev_sum = sum(data[0:3])
    i = 3
    while (i < len(data)):
        curr_sum = sum(data[i-2:i+1])
        if curr_sum > prev_sum:
            counter += 1
        prev_sum = curr_sum
        i += 1
    return counter
    

def main():
    data = parse(FILENAME, 'INT')
    count = puzzle1(data)
    print(f"puzzle 1: {count}")

    count = puzzle2(data)
    print(f"puzzle 2: {count}")

main()