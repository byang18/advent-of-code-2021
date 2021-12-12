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

def times_visited(node, curr_path):
    count = 0
    for n in curr_path:
        if n == node:
            count += 1
    return count
            
def backtrack(curr_node, target, curr_path, paths, graph):
    if curr_node == target:
        if curr_path not in paths:
            paths.append(curr_path.copy())
        return
    for node in graph[curr_node]:
        if node in curr_path and not node.isupper():
            continue
        curr_path.append(node)
        backtrack(node, target, curr_path, paths, graph)
        curr_path.pop()

def puzzle1(data):
    graph = build_graph(data)
    paths = []
    backtrack("start", "end", ["start"], paths, graph)
    return len(paths)

FILENAME = "test.txt"

if __name__ == "__main__":
    data = parse(FILENAME)
    driver(puzzle1, data=data, p=1)
