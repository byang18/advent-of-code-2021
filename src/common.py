import os
from datetime import datetime

class CustomException(Exception):
    pass

def parse(file_name, data_type='STRING'):
    if data_type not in ['STRING', 'INT']:
        raise CustomException("Parameter `data_type` needs to be 'STRING' OR 'INT'")

    res = []
    file_path = os.path.join(os.getcwd(), "data", file_name)
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if data_type == 'INT':
                res.append(int(line.strip()))
            else:
                res.append(line.strip())  
    return res

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

def out_of_mat_bounds(coor, mat):
    i = coor[0]
    j = coor[1]
    if (i == 0 or i == len(mat) - 1 or j == 0 or j == len(mat[0]) - 1):
        return True
    return False

def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if out_of_mat_bounds((i,j), mat):
                continue
            print(f"{mat[i][j]} ", end='')
        print()

def driver(fn, **kwargs):
    time = datetime.now()
    res = fn(kwargs["data"])
    num = kwargs["p"]
    print(f"puzzle{num}: {res}, runtime: {datetime.now() - time}")