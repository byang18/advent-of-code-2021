from common import parse, driver
from math import prod

HEX_TO_BIN = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}

LIT_DICT = {} # maps id to value
OP_DICT = {} # maps (id, version) to children of ids

def get_version_and_type(s):
    return int(s[0:3], 2), int(s[3:6], 2)

def find_literal(s):
    l = ""
    start = 6
    while (start+5 <= len(s)):
        l += s[start:start+5][1:]
        if (s[start:start+5][0] == '0'):
            break
        start += 5
    return int(l, 2), s[start+5:]

def process_nums(t, arr):
    if t == 0:
        return sum(arr)
    if t == 1:
        return prod(arr)
    if t == 2:
        return min(arr)
    if t == 3:
        return max(arr)
    if t == 5:
        return 1 if arr[0] > arr[1] else 0
    if t == 6:
        return 1 if arr[0] < arr[1] else 0
    if t == 7:
        return 1 if arr[0] == arr[1] else 0

def find_packets(s, count, isCount):
    if len(s) < 6 or int(s) == 0:
        return []
    if isCount[0] and count > isCount[1]:
        return []
    v, t = get_version_and_type(s)
    res = []
    if t == 4:
        l, leftover = find_literal(s)
        res.append(l)
        res.extend(find_packets(leftover, count+1, isCount))
        return res
    else:
        if s[6] == '0': # next 15 bits are subpackets len
            length = int(s[7:22], 2)
            res.extend(find_packets(s[22:22+length], count+1, isCount))
            res.extend(find_packets(s[22+length:], count+1, isCount))
        elif s[6] == '1': # next 11 bits are subpackets num
            num_packets = int(s[7:18], 2)
            res.extend(find_packets(s[18:], 0, (True, num_packets)))
        return [process_nums(t, res)]

def puzzle2(data):
    data_bin = ''.join([HEX_TO_BIN[char] for char in data])
    res = find_packets(data_bin, 0, (False, -1))
    return res[0]

FILENAME = "test.txt"
data = parse(FILENAME)[0]
driver(puzzle2, data=data, p=1)