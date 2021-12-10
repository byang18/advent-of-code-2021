from common import parse, driver

VALID_CHUNKS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

SCORES_HASH = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

AC_SCORES_HASH = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def process_corrupted(data):
    scores = [] # ), ], }, >
    incompletes = set([line for line in data])

    for line in data:
        stack = []
        for char in line:
            if char in VALID_CHUNKS:
                stack.append(char)
            else:
                end_char = stack.pop()
                if VALID_CHUNKS[end_char] != char:
                    scores.append(char)
                    incompletes.remove(line)
                    break

    return scores, incompletes

def puzzle1(data):
    scores, _ = process_corrupted(data)
    return sum([SCORES_HASH[char] for char in scores])

def puzzle2(data):
    _, incompletes = process_corrupted(data)
    scores = []
    for line in incompletes:
        stack = []
        for char in line:
            stack.append(char) if char in VALID_CHUNKS else stack.pop()
        completion_string = [VALID_CHUNKS[e] for e in reversed(stack)]
        s = 0
        for char in completion_string:
            s = (s * 5) + AC_SCORES_HASH[char]
        scores.append(s)

    mid = len(scores) // 2
    return sorted(scores)[mid]

FILENAME = "day10.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, p=1)
    driver(puzzle2, data=data, p=2)