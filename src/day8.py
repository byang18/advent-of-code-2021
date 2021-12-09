from common import parse, driver
from day7 import FILENAME

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

def count_segments(inputs, res):
    counts = {}
    for char_string in inputs:
        for char in char_string:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

    segment_counts = [''] * 7 # t, tl, tr, m, bl, br, b
    for char, count in counts.items():
        if count == 6:
            segment_counts[1] = char
        if count == 4:
            segment_counts[4] = char
        if count == 9:
            segment_counts[5] = char

    segment_counts[2] = (set(res[1]) - set(segment_counts[5])).pop()
    return segment_counts

def process_fives(fives, segment_counts, res):
    char_counts = {}
    # process 5s
    for char_string in fives.copy():
        for char in char_string:
            # 5
            if char == segment_counts[1]:
                res[5] = sorted(list(char_string))
                fives.remove(char_string)
                # 2
            if char == segment_counts[4]:
                res[2] = sorted(list(char_string))
                fives.remove(char_string)
    # 3
    res[3] = sorted(list(fives.pop()))

def process_sixes(sixes, segment_counts, res):
    # find 9
    for char_string in sixes.copy():
        missing_char = (set('abcdefg') - set(char_string)).pop()
        if missing_char == segment_counts[4]:
            # 9
            res[9] = sorted(list(char_string))
            sixes.remove(char_string)
        if missing_char == segment_counts[2]:
            res[6] = sorted(list(char_string))
            # 6
            sixes.remove(char_string)
    # 0
    res[0] = sorted(list(sixes.pop()))

def generate_decoder(inputs):
    """
    given a list of inputs, return an array with the indices corresponding to each segment
    """
    res = [''] * 10
    fives = set()
    sixes = set()

    for char_string in inputs:
        if len(char_string) in UNIQUE_LENS:
            res[UNIQUE_LENS[len(char_string)]] = sorted(list(char_string))
        if len(char_string) == 5:
            fives.add(char_string)
        if len(char_string) == 6:
            sixes.add(char_string)

    segment_counts = count_segments(inputs, res)
    process_fives(fives, segment_counts, res)
    process_sixes(sixes, segment_counts, res)
    return res

def decode(code_key, outputs):
    num = ''
    for coded_string in outputs:
        i = code_key.index(sorted(coded_string))
        num += str(i)
    return int(num)
        
def puzzle2(data):
    s = 0
    for line in data:
        inputs =  line.strip().split("|")[0].strip().split()
        outputs = line.strip().split("|")[1].strip().split()
        code_key = generate_decoder(inputs)
        num = decode(code_key, outputs)
        s += num
    return s
        

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, p=1)
    driver(puzzle2, data=data, p=2)