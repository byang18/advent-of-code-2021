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

def driver(fn, **kwargs):
    time = datetime.now()
    res = fn(kwargs["data"])
    num = kwargs["n"]
    print(f"puzzle{num}: {res}, runtime: {datetime.now() - time}")