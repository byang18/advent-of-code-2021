from collections import deque
from common import parse, build_matrix, out_of_mat_bounds, driver

def flash(coors, to_flash, flashed, mat):
    i = coors[0]
    j = coors[1]
    neighbors = [
        (i-1, j-1),
        (i-1, j),
        (i-1, j+1),
        (i, j-1),
        (i, j+1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1)
    ]
    for neighbor in neighbors:
        ni = neighbor[0]
        nj = neighbor[1]
        if out_of_mat_bounds((ni, nj), mat):
                continue
        if neighbor not in to_flash and neighbor not in flashed:
            ni = neighbor[0]
            nj = neighbor[1]
            mat[ni][nj] += 1
            if mat[ni][nj] > 9:
                to_flash.append(neighbor)
    flashed.append((i, j))

def step(mat):
    flashed = []

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if out_of_mat_bounds((i, j), mat):
                continue
            mat[i][j] += 1
            # check for flash
            if mat[i][j] > 9 and (i, j) not in flashed:
                to_flash = deque()
                to_flash.append((i, j))
                while (len(to_flash) > 0):
                    popped_coor = to_flash.popleft()
                    flash(popped_coor, to_flash, flashed, mat)
    
    # set all flashed to 0
    for coor in flashed:
        i = coor[0]
        j = coor[1]
        mat[i][j] = 0

    return flashed

def puzzle1(data):
    num_steps = 100
    flash_count = 0
    mat = build_matrix(data)
    for i in range(num_steps):
        flashed = step(mat)
        flash_count += len(flashed)
    return flash_count

def puzzle2(data):
    mat = build_matrix(data)
    i = 1
    while(True):
        flashed = step(mat)
        if len(flashed) == len(mat) * len(mat[0]):
            return i
        i += 1

FILENAME = "day11.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, p=1)
    driver(puzzle2, data=data, p=2)