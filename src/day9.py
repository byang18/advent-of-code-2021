from common import parse, driver
from collections import deque

def build_matrix(data):
    mat = []
    for line in data:
        row = [9]
        for char in line:
            row.append(int(char))
        row.append(9)
        mat.append(row)
    mat.insert(0, [9] * len(mat[0]))
    mat.append([9] * len(mat[0]))
    return mat

def find_lowest(mat):
    s = 0
    coors = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i == 0 or i == len(mat) - 1 or j == 0 or j == len(mat[0]) - 1):
                continue
            neighbors = [
                mat[i-1][j],
                mat[i][j+1],
                mat[i+1][j],
                mat[i][j-1]
            ]
            if mat[i][j] < min(neighbors):
                coors.append((i, j))
                s += mat[i][j] + 1
    return s, coors

def puzzle1(mat):
    s, _ = find_lowest(mat)
    return s

# given matrix, starting coordinate, return coordinates of basin
def bfs(start_coor, mat, basins):
    basin = set()
    q = deque() # mark visit
    q.append(start_coor)

    while (len(q) > 0):
        coor = q.popleft()
        basin.add(coor)
        i = coor[0]
        j = coor[1]
        neighbors = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
        for neighbor in neighbors:
            nx = neighbor[0]
            ny = neighbor[1]
            if mat[nx][ny] == 9:
                continue
            if neighbor not in basin:
                basin.add(neighbor)
                q.append(neighbor)
    
    basins.append(basin)
    return len(basin)

def puzzle2(mat):
    _, coors = find_lowest(mat)
    basins = []
    sizes = []
    for coor in coors:
        size = bfs(coor, mat, basins)
        sizes.append(size)
    sizes = sorted(sizes, reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

FILENAME = "day9.txt"

if __name__ == "__main__":
    mat = build_matrix(parse(FILENAME))
    driver(puzzle1, data=mat, p=1)
    driver(puzzle2, data=mat, p=2)