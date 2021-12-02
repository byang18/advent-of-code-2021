from common import parse, CustomException

FILENAME = "day2.txt"

def puzzle1(data):
    x = 0 # horizontal
    y = 0 # vertical

    for action in data:
        a = action.strip().split(' ')
        if (a[0] == 'forward'):
            x += int(a[1])
        elif (a[0] == 'up'):
            y -= int(a[1])
        elif (a[0] == 'down'):
            y += int(a[1])
        else:
            raise CustomException(f"command `{a}` not valid")

    return x * y

def puzzle2(data):
    x = 0
    y = 0
    aim = 0

    for action in data:
        a = action.strip().split(' ')
        if (a[0] == 'up'):
            aim -= int(a[1])
        elif (a[0] == 'down'):
            aim += int(a[1])
        elif (a[0] == 'forward'):
            x += int(a[1])
            y += int(a[1]) * aim
        else:
            raise CustomException(f"command `{a}` not valid")
    
    return x * y


def main():
    data = parse(FILENAME)
    res = puzzle1(data)
    print(f"puzzle 1: {res}")

    res = puzzle2(data)
    print(f"puzzle 2: {res}")

main()