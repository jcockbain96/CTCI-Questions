from collections import deque


def recreate_path(start, end, last_node):
    curr = end
    res = []
    while curr != start:
        res.append(curr)
        curr = last_node[curr]
    return [start] + res[::-1]


def route_between_nodes(graph, start, end):
    queue = deque([start])
    last_node = {}
    while queue:
        node = queue.popleft()
        if node == end:
            return recreate_path(start, end, last_node)
        for neighbour in graph[node]:
            if neighbour not in last_node:
                queue.append(neighbour)
                last_node[neighbour] = node
    raise ValueError("No Valid Path")

