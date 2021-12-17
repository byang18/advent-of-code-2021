from common import parse, driver

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

def get_version_and_type(s):
    return int(s[0:3], 2), int(s[3:6], 2)

def find_literal(s):
    v, t = get_version_and_type(s)
    l = ""
    start = 6
    while (start+5 <= len(s)):
        l += s[start:start+5]
        if (s[start:start+5][0] == '0'):
            break
        start += 5
    return int(l, 2), s[start+5:]

def find_packets(s, res):
    if len(s) < 6 or int(s) == 0:
        return
    v, t = get_version_and_type(s)
    if t == 4:
        l, leftover = find_literal(s)
        find_packets(leftover, res)
    else: 
        if s[6] == '0': # next 15 bits are subpackets len
            length = int(s[7:22], 2)
            find_packets(s[22:], res)
            # find_packets(s[22+length+1:], res)
        elif s[6] == '1': # next 11 bits are subpackets num
            num_packets = int(s[7:18], 2)
            find_packets(s[18:], res)
    res.append((v, t, s))

def puzzle1(data):
    data_bin = ''.join([HEX_TO_BIN[char] for char in data])
    res = []
    find_packets(data_bin, res)
    for id, t, data in res:
        print(f"id: {id}; type: {t}; data: {data}")
    return sum([id for id, _, _ in res])

FILENAME = "test.txt"
data = parse(FILENAME)[0]
driver(puzzle1, data=data, p=1)