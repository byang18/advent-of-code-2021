from common import parse, driver

def build_graph(data):
    graph = {}
    for line in data:
        node_names = line.strip().split('-')
        n1_name = node_names[0]
        n2_name = node_names[1]

        if n1_name not in graph:
            graph[n1_name] = set([n2_name])
        if n2_name not in graph:
            graph[n2_name] = set([n1_name])
        
        graph[n1_name].add(n2_name)
        graph[n2_name].add(n1_name)
    return graph

def cant_double(curr_path):
    visited = set()
    for node in curr_path:
        if not node.isupper() and node in visited:
            return True
        visited.add(node)
    return False
            
def backtrack(curr_node, target, curr_path, paths, graph):
    if curr_node == target:
        if curr_path not in paths:
            paths.append(curr_path.copy())
        return
    for node in graph[curr_node]:
        if node in curr_path and not node.isupper():
            if node == "start" or node == "end":
                continue
            if cant_double(curr_path):
                continue
        curr_path.append(node)
        backtrack(node, target, curr_path, paths, graph)
        curr_path.pop()

def puzzle2(data):
    graph = build_graph(data)
    paths = []
    backtrack("start", "end", ["start"], paths, graph)
    return len(paths)

FILENAME = "day12.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle2, data=data, p=2)
