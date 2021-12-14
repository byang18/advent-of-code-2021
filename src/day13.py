from common import parse, driver
from common import print_matrix

def parse_day13(data):
    coors = []
    commands = []
    largest_y = 0
    largest_x = 0
    for line in data:
        if line.strip() == '':
            continue
        if line.strip().startswith("fold"):
            commands.append(line.strip().split('fold along ')[1])
        else:
            x, y = line.strip().split(',')
            largest_x = max(largest_x, int(x))
            largest_y = max(largest_y, int(y))
            coors.append((int(x), int(y)))
    return coors, commands, largest_x, largest_y   

def build_matrix(coors, l_x, l_y):
    mat = []
    for y in range(l_y + 1):
        row = []
        for x in range(l_x + 1):
            row.append('.')
        mat.append(row)
    for coor in coors:
        x = coor[0]
        y = coor[1]
        mat[y][x] = '#'
    return mat

# finds which lines are "twinned" according to the fold
def find_pairs(command, mat):
    axis, fold_num = command.split('=')
    fold_num = int(fold_num)
    pairs = []
    i = fold_num
    j = fold_num
    l = len(mat) if axis == 'y' else len(mat[0])
    while (i >= 0 and j < l):
        if (i != fold_num):
            pairs.append((i, j))
        i -= 1
        j += 1
    return i, pairs

def execute_command(command, mat):
    start, pairs = find_pairs(command, mat)
    axis, fold_num = command.split('=')
    new_pairs = []
    if axis == 'y':
        if start != 0:
            for y in range(start):
                for x in range(len(mat[0])):
                    if mat[y][x] == '#':
                        new_pairs.append((x, y))
        for pair in pairs:
            for x in range(len(mat[0])):
                my_row = pair[0]
                if mat[my_row][x] == '#' or mat[pair[1]][x] == '#':
                    new_pairs.append((x, my_row))
        new_mat = build_matrix(new_pairs, len(mat[0]), int(fold_num) - 1)
    else:
        print("x axis now!")
        if start != 0:
            for x in range(start):
                for y in range(len(mat)):
                    if mat[y][x] == '#':
                        new_pairs.append((x, y))
        for pair in pairs:
            for y in range(len(mat)):
                my_col = pair[0]
                if mat[y][my_col] == '#' or mat[y][pair[1]] == '#':
                    new_pairs.append((my_col, y))
        new_mat = build_matrix(new_pairs, int(fold_num) - 1, len(mat))
    print_matrix(new_mat)
                
    return len(new_pairs), new_mat

def puzzle2(data):
    coors, commands, l_x, l_y = parse_day13(data)
    mat = build_matrix(coors, l_x, l_y)
    for command in commands:
        s, new_mat = execute_command(command, mat)
        mat = new_mat
    return s

FILENAME = "day13.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle2, data=data, p=1)