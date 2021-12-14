from common import parse, driver

STEPS = 40

def build_map_p1(commands):
    rules = {}
    for command in commands:
        if command == '':
            continue
        pair, insert_elem = command.strip().split(' -> ')
        rules[pair] = pair[0] + insert_elem + pair[1]
    return rules

def step_p1(polymer, rules):
    new_str = ''
    prev_edited = False
    i = 1
    while (i < len(polymer)):
        pair = polymer[i-1:i+1]
        if pair in rules:
            if not prev_edited:
                new_str = new_str + rules[pair]
            else:
                new_str = new_str + rules[pair][1:]
            prev_edited = True
        else:
            prev_edited = False
        i += 1
    return new_str

def solve_p1(polymer):
    chars = [0] * 128
    for char in polymer:
        chars[ord(char)] += 1
    return max(chars) - min([count for count in chars if count != 0])

def puzzle1(data):
    polymer = data.pop(0)
    rules = build_map_p1(data)
    for i in range(1, STEPS + 1):
        polymer = step_p1(polymer, rules)
        # print(f"step {i}: {len(polymer)}")
    return solve_p1(polymer)

#### PUZZLE 2

def build_map_p2(data):
    rules = {}
    for line in data:
        if line.strip() != '':
            rule, value = line.strip().split(' -> ')
            rules[rule] = value
    return rules

def puzzle2(data):
    polymer = data.pop(0)
    rules = build_map_p2(data)
    state  = {pair: 0 for pair in rules.keys()}
    scores = {char: 0 for char in set(rules.values())}

    # generate starting frequencies
    for i in range(1, len(polymer)):
        state[polymer[i-1:i+1]] += 1
    for i in range(len(polymer)):
        scores[polymer[i]] += 1

    for i in range(STEPS):
        next_state = {pair: 0 for pair in rules.keys()}
        for key, value in state.items():
            new_char = rules[key]
            next_state[key[0] + new_char] += value
            next_state[new_char + key[1]] += value
            scores[new_char] += value
        state = next_state
    
    return max(scores.values()) - min(scores.values())

FILENAME = "day14.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    # driver(puzzle1, data=data.copy(), p=1)
    driver(puzzle2, data=data.copy(), p=2)