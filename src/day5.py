from common import parse, driver
from day4 import create_boards

MAX_SIZE = 1000
FILENAME = "day5.txt"

def print_board(board):
    for row in board:
        for val in row:
            if val != 0:
                print(val, end=' ')
            else:
                print('.', end=' ')
        print()

def create_board():
    board = []
    for i in range(MAX_SIZE):
        row = []
        for j in range(MAX_SIZE):
            row.append(0)
        board.append(row)
    return board

def get_coors(line):
    arr = line.strip().replace(" -> ", ',').split(',')
    return (int(arr[0]), int(arr[1])), (int(arr[2]), int(arr[3]))

def get_total(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in [0, 1]:
                total += 1
    return total

def move1(line, board):
    start_pos, end_pos = get_coors(line)
    
    # need to move hoizontally
    if (start_pos[0] == end_pos[0]):
        max_x_pos = max(start_pos[1], end_pos[1])
        min_x_pos = min(start_pos[1], end_pos[1])
        for j in range(min_x_pos, max_x_pos + 1):
            board[j][start_pos[0]] += 1
    
     # need to move vertically
    elif (start_pos[1] == end_pos[1]):
        max_y_pos = max(start_pos[0], end_pos[0])
        min_y_pos = min(start_pos[0], end_pos[0])
        for i in range(min_y_pos, max_y_pos + 1):
            board[start_pos[1]][i] += 1

def move2(line, board):
    start_pos, end_pos = get_coors(line)

    # need to move hoizontally
    if (start_pos[0] == end_pos[0]):
        max_x_pos = max(start_pos[1], end_pos[1])
        min_x_pos = min(start_pos[1], end_pos[1])
        for j in range(min_x_pos, max_x_pos + 1):
            board[j][start_pos[0]] += 1
    
     # need to move vertically
    elif (start_pos[1] == end_pos[1]):
        max_y_pos = max(start_pos[0], end_pos[0])
        min_y_pos = min(start_pos[0], end_pos[0])
        for i in range(min_y_pos, max_y_pos + 1):
            board[start_pos[1]][i] += 1

    else:
        vert_dir = 1 if start_pos[0] < end_pos[0] else -1
        hor_dir = 1 if start_pos[1] < end_pos[1] else -1
        y = start_pos[0]
        x = start_pos[1]
        while((y, x) != end_pos):
                board[x][y] += 1
                y += vert_dir
                x += hor_dir
        board[x][y] += 1

def puzzle1(data):
    board = create_board()
    for line in data:
        move1(line, board)
    total = get_total(board)
    return total

def puzzle2(data):
    board = create_board()
    for line in data:
        move2(line, board)
    total = get_total(board)
    return total

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=list(data), p=1)
    driver(puzzle2, data=list(data), p=1)