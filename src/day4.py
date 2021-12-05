from datetime import datetime
from common import parse, driver

def create_boards(data):
    board_num = -1
    boards = []
    for line in data:
        stripped_line = line.strip()

        # reset the board
        if stripped_line == "":
            board_num += 1
            boards.append([])
            continue

        row = stripped_line.split()
        boards[board_num].append(row)
    return boards

def mark_board(command, board):
    total = 0
    for i in range(len(board)): # row num
        for j in range(len(board[0])): # col num
            char = board[i][j]
            if char  == str(command):
                board[i][j] = '.'
            elif char != '.':
                total += int(board[i][j])
    return total
    

def check_board(board):
    # check rows
    for row in board:
        count = 0
        for char in row:
            if char == '.':
                count += 1
        if count == len(board):
            return True
    
    # check cols
    for j in range(len(board[0])):
        count = 0
        for i in range(len(board)):
            if board[i][j] == '.':
                count += 1
        if count == len(board[0]):
            return True
    
    return False

def puzzle1(data):
    commands = data.pop(0).split(",")
    boards = create_boards(data)

    for i, command in enumerate(commands):
        for j, board in enumerate(boards):
            # print(f"command: {command}, board: {j}")
            total = mark_board(command, board)
            if check_board(board):
                return total * int(command)

def puzzle2(data):
    commands = data.pop(0).split(",")
    boards = create_boards(data)
    boards_set = set([i for i in range(len(boards))])
    flag = False

    for command in commands:
        for j, board in enumerate(boards):
            if j not in boards_set:
                continue
            # print(f"command: {command}, board: {j}, l: {len(boards)}")
            total = mark_board(command, board)
            if check_board(board):
                boards_set.remove(j)
                if len(boards_set) == 1:
                    flag = True
                    continue
            if flag and check_board(board):
                return total * int(command)

FILENAME = "day4.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=list(data), p=1)
    driver(puzzle2, data=list(data), p=2)
