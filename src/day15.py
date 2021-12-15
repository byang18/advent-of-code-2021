from common import parse, driver
from common import build_matrix, get_all_coors, out_of_mat_bounds
from common import print_matrix

def get_neighbors(coor, mat):
    i = coor[0]
    j = coor[1]
    neighbors = [
        (i-1, j),
        (i, j-1),
        (i+1, j),
        (i, j+1)
    ]
    return [coor for coor in neighbors if not out_of_mat_bounds(coor, mat)]

def pq_add(elem, pq):
    for priority, data in pq.copy():
        if elem[1] == data:
            pq.remove((priority, data))
            break
    pq.append(elem)
    pq.sort(reverse=True)

def dijkstra(start, mat):
    visited = {coor:float("inf") for coor in get_all_coors(mat)}
    visited[start] = 0
    pq = [(0, start)]
    while (len(pq) > 0):
        _, coor = pq.pop()
        
        # relax
        for neighbor in get_neighbors(coor, mat):
            # the cost in the visited is too large, so update
            if (visited[neighbor] > visited[coor] + mat[neighbor[0]][neighbor[1]]):
                visited[neighbor] = visited[coor] + mat[neighbor[0]][neighbor[1]]
                pq_add((visited[neighbor], neighbor), pq)
    return visited

def puzzle1(data):
    mat = build_matrix(data)
    start = (0, 0)
    visited = dijkstra(start, mat)
    coor = (len(mat)-1, len(mat[0])-1)
    return visited[coor]

def build_matrix_p2(data):
    mat = build_matrix(data)

    # initialize
    new_mat = []
    for i in range(len(mat) * 5):
        new_row = [0] * len(mat[0]) * 5
        new_mat.append(new_row)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_mat[i][j] = mat[i][j]

    # update first 5 rows
    offset = len(mat[0])
    for i in range(4):
        for x in range(offset, offset + len(mat[0])):
            for y in range(len(mat)):
                new_val = new_mat[y][x - len(mat[0])] + 1
                new_mat[y][x] = new_val if new_val < 10 else 1
        offset += len(mat[0])

    # update rest of the rows
    offset = len(mat[0])
    for i in range(4):
        for y in range(offset, offset + len(mat)):
            for x in range(len(new_mat[0])):
                new_val = new_mat[y - len(mat)][x] + 1
                new_mat[y][x] = new_val if new_val < 10 else 1
        offset += len(mat[0])
    
    return new_mat

def puzzle2(data):
    mat = build_matrix_p2(data)
    start = (0, 0)
    visited = dijkstra(start, mat)
    coor = (len(mat)-1, len(mat[0])-1)
    return visited[coor]

FILENAME = "day15.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, p=1)
    driver(puzzle2, data=data, p=2)