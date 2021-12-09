from common import parse, driver
from day7 import FILENAME

MAP = {
    1: 4,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

UNIQUE_LENS = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

FILENAME = "day8.txt"

def puzzle1(data):
    count = 0
    for line in data:
        outputs = line.strip().split("|")[1].strip().split()
        for output in outputs:
            if len(output) in UNIQUE_LENS:
                count += 1    
    return count

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, p=1)