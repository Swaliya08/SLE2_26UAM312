from collections import deque
import timeit

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


# BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(path + [neighbour])

    return None, nodes_expanded


# DFS
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(path + [neighbour])

    return None, nodes_expanded


# Run BFS
bfs_path, bfs_nodes = bfs(graph, 'A', 'G')

# Run DFS
dfs_path, dfs_nodes = dfs(graph, 'A', 'G')


# Measure execution time
bfs_time = timeit.timeit(
    lambda: bfs(graph, 'A', 'G'),
    number=1000
)

dfs_time = timeit.timeit(
    lambda: dfs(graph, 'A', 'G'),
    number=1000
)


# Convert seconds to milliseconds
bfs_avg_time = (bfs_time / 1000) * 1000
dfs_avg_time = (dfs_time / 1000) * 1000


# Display results
print("----- BFS RESULTS -----")
print("Path:", bfs_path)
print("Nodes Expanded:", bfs_nodes)
print("Average Time:", bfs_avg_time, "ms")

print("\n----- DFS RESULTS -----")
print("Path:", dfs_path)
print("Nodes Expanded:", dfs_nodes)
print("Average Time:", dfs_avg_time, "ms")