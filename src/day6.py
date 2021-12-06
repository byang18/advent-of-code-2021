from common import parse, driver

FILENAME = "day6.txt"

def increment_day(state):
    res = []
    zero_count = 0
    for num in state:
        new_num =  num - 1
        if new_num < 0:
            new_num = 6
            zero_count += 1
        res.append(new_num)
    for i in range(zero_count):
        res.append(8)
    return res

def puzzle1(state):
    days = 80
    for i in range(days):
        # print(f"{i}: {state}")
        new_state = increment_day(state)
        state = new_state
    return len(state)

def puzzle2(data):
    days = 256
    states = [0] * 9

    for num in data:
        states[num] += 1

    for i in range(days):
        # print(f"day {i}: {states}")

        # first, decrement all values
        num_zeros = states[0] # number of zeros
        for j in range(8):
            states[j] = states[j+1]

        # perform additional functions
        states[6] += num_zeros
        states[8] = num_zeros

    return sum(states)

if __name__ == "__main__":
    data = [int(x) for x in parse(FILENAME)[0].strip().split(',')]
    # driver(puzzle1, data=data, p=1)
    driver(puzzle2, data=data, p=2)