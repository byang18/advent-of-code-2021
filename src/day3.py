from common import parse, driver, CustomException

def _convert_bin_to_dec(n):
    i = 0
    res = 0
    while (i < len(n)):
        exponent = len(n) - i - 1
        res += (2 ** exponent) * int(n[i])
        i += 1
    return res

def _get_data_counts(data):
    counts = [0] * len(data[0])
    for bn in data:
        for i in range(len(bn)):
            if bn[i] == '1':
                counts[i] += 1
            else:
                counts[i] -= 1
    return counts

def puzzle1(data):
    # assume all binary numbers are same length
    gamma = [0] * len(data[0])
    epsilon = [0] * len(data[0])
    counts = _get_data_counts(data)

    for i in range(len(counts)):
        if counts[i] > 1:
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma_dec = _convert_bin_to_dec(gamma)
    epsilon_dec = _convert_bin_to_dec(epsilon)

    return gamma_dec * epsilon_dec

def _get_count_by_index(data, index):
    count = 0
    for bn in data:
        if bn[index] == '1':
            count += 1
        else:
            count -= 1
    return count

def _keep_valids(universe, index, *args):
    res = _get_count_by_index(universe, index)
    val = args[0] if res >= 0 else args[1]
    for bn in universe.copy():
        if bn[index] != val:
            universe.remove(bn)

def puzzle2(data):
    o_universe = set(data)
    i = 0
    while(len(o_universe) > 1 and i < len(data[0])):
        _keep_valids(o_universe, i, '1', '0')
        i += 1

    co_universe = set(data)
    i = 0
    while(len(co_universe) > 1 and i < len(data[0])):
        _keep_valids(co_universe, i, '0', '1')
        i += 1

    if len(o_universe) > 0:
        o = o_universe.pop()
        o_dec = _convert_bin_to_dec(o)
    else:
        raise CustomException("O universe has more than 1 value")

    if len(co_universe) > 0:
        co = co_universe.pop()
        co_dec = _convert_bin_to_dec(co)
    else:
        raise CustomException("CO universe has more than 1 value")
 
    return o_dec * co_dec
    
####

FILENAME = "day3.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, n=1)
    driver(puzzle2, data=data, n=2)
    